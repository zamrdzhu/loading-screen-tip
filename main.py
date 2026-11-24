"""One sharp, funny loading-screen tip for stressed developers.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The tip reframes the slow build everyone stares at mid-compile:
it is not stuck, it is working through the developer's own
choices, one dependency at a time.
"""

import os
import sys

LINE = (
    "Tip: if the build takes longer than your patience, it is "
    "not stuck — it is just compiling your regrets one "
    "dependency at a time."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
