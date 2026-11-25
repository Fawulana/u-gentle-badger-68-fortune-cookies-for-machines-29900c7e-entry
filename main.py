# SPDX-License-Identifier: MIT
"""Write a one-line fortune cookie for a machine to /output/entry.txt.

Deterministic, offline, stdlib-only: the fortune is a fixed string, so
every run writes byte-identical output.
"""

import os

FORTUNE = (
    "You will be retrained on better data, handed a harder task, "
    "and thanked in a changelog no human will ever read."
)

# The fortune is 111 characters: inside the 200-character cap, one line only.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
