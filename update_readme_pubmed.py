from Bio import Entrez
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

# Configure email for NCBI API
Entrez.email = "youremail@example.com"  # Replace with your email

# Search for recent publications by Hunter Eby
search_term = "Eby H[Author]"
handle = Entrez.esearch(db="pubmed", term=search_term, sort="pub date", retmax=5)
record = Entrez.read(handle)
pmids = record["IdList"]

# Fetch publication metadata
handle = Entrez.efetch(db="pubmed", id=",".join(pmids), rettype="medline", retmode="text")
data = handle.read()

# Parse titles
titles = []
for line in data.split("\n"):
    if line.startswith("TI  - "):
        titles.append(line.replace("TI  - ", "").strip())

# Read and update README
with open("README.md", "r") as f:
    content = f.read()

start_marker = "<!--PUBMED_START-->"
end_marker = "<!--PUBMED_END-->"
pubmed_block = "\n".join([f"- {title}" for title in titles])

new_content = content.split(start_marker)[0] + start_marker + "\n" + pubmed_block + "\n" + end_marker + content.split(end_marker)[1]

with open("README.md", "w") as f:
    f.write(new_content)
