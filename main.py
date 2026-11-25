"""Midnight Fridge Roast — make.fun entry.

One original one-line roast of a smart fridge that refuses to open
after midnight, playing on the fridge as a nightclub bouncer who
recognises its regular and still turns him away at the door.
Writes the single roast line (under 200 characters, exactly one line)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = (
    "My fridge won't open after midnight \u2014 it's the only bouncer "
    "who knows my name and still won't let me in."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE.strip(), "entry must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} chars to {path}:")
    print(LINE)


if __name__ == "__main__":
    main()
