#!/usr/bin/env python3
"""Update Google Scholar citation information in README.md."""

from __future__ import annotations

import re
from pathlib import Path
from typing import List

from scholarly import scholarly

USER_ID = "rFZAeeEAAAAJ"
README_PATH = Path(__file__).resolve().parent / "README.md"


def fetch_scholar_data(user_id: str) -> tuple[int, int, List[str]]:
    """Return citation count, h-index, and list of recent publication titles."""
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["indices", "publications"])

    citation_count = author.get("citedby", 0)
    h_index = author.get("hindex", 0)
    publications = [
        pub["bib"].get("title", "")
        for pub in author.get("publications", [])[:3]
    ]
    return citation_count, h_index, publications


def update_readme(citations: int, h_index: int, pubs: List[str]) -> None:
    """Replace placeholders in README with fetched scholar data."""
    text = README_PATH.read_text()

    text = re.sub(
        r"Google_Scholar-(?:\d+|\{\{CITATION_COUNT\}\})_citations",
        f"Google_Scholar-{citations}_citations",
        text,
    )
    text = re.sub(
        r"h--index-(?:\d+|\{\{H_INDEX\}\})",
        f"h--index-{h_index}",
        text,
    )

    pub_lines = "\n".join(f"- {p}" for p in pubs)
    text = re.sub(
        r"### Recent Publications\n(?:-.*\n)*",
        f"### Recent Publications\n{pub_lines}\n",
        text,
    )

    README_PATH.write_text(text)


def main() -> None:
    citations, h_index, pubs = fetch_scholar_data(USER_ID)
    update_readme(citations, h_index, pubs)


if __name__ == "__main__":
    main()
