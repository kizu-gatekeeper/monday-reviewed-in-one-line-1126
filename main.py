"""Entry for make.fun bounty: Monday, Reviewed in One Line.

Writes a single line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = "★☆☆☆☆ — Monday arrived uninvited, drank my motivation straight from the carton, and left five meetings in my calendar like raccoons in a bin. Would not rebook."
MAX_CHARS = 200


def write_entry(out_dir: str) -> Path:
    assert LINE and LINE.strip() == LINE, "entry must be a single non-empty line"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "entry.txt"
    path.write_text(LINE, encoding="utf-8")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
