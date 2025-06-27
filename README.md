from scholarly import scholarly

# Your Google Scholar ID
user_id = "rFZAeeEAAAAJ"

# Fetch author data
author = scholarly.search_author_id(user_id)
author = scholarly.fill(author, sections=["indices"])

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
