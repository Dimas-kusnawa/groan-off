"""The One-Liner Groan-Off — one dad joke, written to /output/entry.txt."""

import os

# The joke: the sweetest dev moment is a first-try compile — and the
# groan is that it was never your code running at all. A real truth,
# insider-specific and concrete, with the twist landing in the last
# words, like the resolved ai-joke winners ("the typo is now
# load-bearing", "Removing the line was the last thing it asked").
LINE = "My code finally compiled on the first try, so I checked the logs - it had been running the old version the whole time."


# Gate: 1-140 UTF-8 characters, single line, no trailing newline.
# This line is 118 characters — well inside the gate.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
