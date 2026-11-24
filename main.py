#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt, where the grader's gate
checks it (UTF-8 text, 1 to 200 characters, not only whitespace)
and the judge reads it.
"""

import os

JOKE = (
    "Our robot vacuum kept bumping into the same chair all morning. "
    "Dad just nodded and said, 'Leave him be, son - he's having "
    "a Roomba awakening.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate takes UTF-8 text of 1 to 200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the gate"
    os.umask(0o022)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
