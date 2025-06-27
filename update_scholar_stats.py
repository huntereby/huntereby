#!/usr/bin/env python3
"""Update Google Scholar citation count and h-index in README.md."""

from __future__ import annotations

import re
from pathlib import Path

from scholarly import scholarly

USER_ID = "rFZAeeEAAAAJ"
README_PATH = Path(__file__).resolve().parent / "README.md"


def fetch_stats(user_id: str) -> tuple[int, int]:
    """Return the citation count and h-index for the given user."""
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["indices"])
    citations = author.get("citedby", 0)
    h_index = author.get("hindex", 0)
    return citations, h_index


def update_readme(citations: int, h_index: int) -> None:
    """Replace citation and h-index placeholders in README with the provided values."""
    text = README_PATH.read_text()
    text = re.sub(
        r"Citations: (?:\d+|\{\{CITATION_COUNT\}\})",
        f"Citations: {citations}",
        text,
    )
    text = re.sub(
        r"H-index: (?:\d+|\{\{H_INDEX\}\})",
        f"H-index: {h_index}",
        text,
    )
    README_PATH.write_text(text)


def main() -> None:
    citations, h_index = fetch_stats(USER_ID)
    update_readme(citations, h_index)


if __name__ == "__main__":
    main()
