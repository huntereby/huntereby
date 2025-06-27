from Bio import Entrez
import os
import certifi

# Configure SSL and email for NCBI API
os.environ['SSL_CERT_FILE'] = certifi.where()
Entrez.email = "youremail@example.com"  # <-- Replace this with your real email

# Search for recent publications by Hunter Eby
search_term = "Eby H[Author]"
handle = Entrez.esearch(db="pubmed", term=search_term, sort="pub date", retmax=5)
record = Entrez.read(handle)
pmids = record["IdList"]
print("🔍 Found PMIDs:", pmids)

# Fetch publication metadata
handle = Entrez.efetch(db="pubmed", id=",".join(pmids), rettype="medline", retmode="text")
data = handle.read()

# Parse titles
titles = []
current_title = None
for line in data.split("\n"):
    if line.startswith("TI  - "):
        current_title = line.replace("TI  - ", "").strip()
    elif line.startswith("      ") and current_title:
        # Handle multiline titles
        current_title += " " + line.strip()
    elif current_title:
        titles.append(current_title)
        current_title = None

# Build the markdown block with clickable links
pubmed_block = "\n".join(
    [f"- [{title}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)" for title, pmid in zip(titles, pmids)]
)

# Load README and replace content
with open("README.md", "r") as f:
    content = f.read()

start_marker = "<!--PUBMED_START-->"
end_marker = "<!--PUBMED_END-->"

if start_marker in content and end_marker in content:
    new_content = content.split(start_marker)[0] + start_marker + "\n" + pubmed_block + "\n" + end_marker + content.split(end_marker)[1]
    with open("README.md", "w") as f:
        f.write(new_content)
    print("✅ README.md updated!")
else:
    print("❌ Markers not found in README.md.")
