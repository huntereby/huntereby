from scholarly import scholarly
import sys

try:
    user_id = "rFZAeeEAAAAJ"
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["basics", "indices"])

    citations = author["citedby"]
    h_index = author["hindex"]
    i10_index = author["i10index"]

    print(f"✅ Citations: {citations}, h-index: {h_index}, i10-index: {i10_index}")

    # Update README
    with open("README.md", "r") as f:
        content = f.read()

    content = content.replace("{{CITATION_COUNT}}", str(citations))
    content = content.replace("{{H_INDEX}}", str(h_index))

    with open("README.md", "w") as f:
        f.write(content)

    print("✅ README.md updated with Google Scholar stats")

except Exception as e:
    print(f"❌ Google Scholar update failed: {e}")
    sys.exit(0)  # Prevents workflow from hanging
