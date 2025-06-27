from scholarly import scholarly

### Links
- [Google Scholar Profile](https://scholar.google.com/citations?user=rFZAeeEAAAAJ)
- [ORCID 0000-0002-9029-9768](https://orcid.org/0000-0002-9029-9768)

*Run `python update_scholar_stats.py` to refresh citation counts automatically.*

citations = author["citedby"]
h_index = author["hindex"]

# Read your README
with open("README.md", "r") as f:
    content = f.read()

# Replace placeholders
content = content.replace("{{CITATION_COUNT}}", str(citations))
content = content.replace("{{H_INDEX}}", str(h_index))

# Write back to README
with open("README.md", "w") as f:
    f.write(content)



<!--
**huntereby/huntereby** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
