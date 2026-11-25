"""One-Liner Marathon entry.

Writes one fixed one-line comedy joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no network, no randomness, no reading anything at runtime.
The winning line is a fixed constant in this file.
"""

import os

LINE = "My password is so secure even I can't log in \u2014 my bank now asks me security questions about a life I don't remember living."


def validate(text):
    """Gate: 1-280 chars, single line, not only whitespace, UTF-8 text."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate(LINE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back gate: the file on disk must be exactly the winning line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    validate(back)


if __name__ == "__main__":
    main()
