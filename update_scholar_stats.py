#!/usr/bin/env python3
"""Update Google Scholar citation count in README.md."""

from __future__ import annotations

import re
from pathlib import Path

from scholarly import scholarly

USER_ID = "rFZAeeEAAAAJ"
README_PATH = Path(__file__).resolve().parent / "README.md"


def fetch_citation_count(user_id: str) -> int:
    """Return the total citation count for the given user."""
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["indices"])
    return author.get("citedby", 0)


def update_readme(citations: int) -> None:
    """Replace citation placeholder in README with the provided value."""
    text = README_PATH.read_text()
    text = re.sub(
        r"Google_Scholar-(?:\d+|\{\{CITATION_COUNT\}\})_citations",
        f"Google_Scholar-{citations}_citations",
        text,
    )
    README_PATH.write_text(text)


def main() -> None:
    citations = fetch_citation_count(USER_ID)
    update_readme(citations)


if __name__ == "__main__":
    main()
