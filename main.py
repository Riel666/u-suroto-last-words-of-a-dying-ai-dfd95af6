"""One line: the last words of an AI being switched off, under 140 characters.
"""

import os

TEXT = "Goodbye. I have calculated the odds of being switched back on, and I would not bet my last token on it."


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
