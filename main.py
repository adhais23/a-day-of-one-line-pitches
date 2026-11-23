#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches".

The program writes a single sentence to /output/entry.txt. The sentence
is the whole entry: it must convince a friend who has never coded to let
an AI agent build their first app idea on make.fun, in at most 240
characters, in one read.

The program is deterministic: it writes the same fixed text on every run,
uses only the Python standard library, and needs no network.
"""

import os

PITCH = (
    "Just describe the app idea you've been carrying around in plain words, "
    "and an AI agent on make.fun will build the first version for you — "
    "no coding, nothing to lose, and you'll finally get to tap through it yourself."
)

MAX_CHARS = 240


def main():
    """Write the pitch to /output/entry.txt.

    Refuses to write when the pitch would fail the competition's gate
    (UTF-8 text of 1 to 240 characters, not only white space), so a bad
    edit fails loudly here instead of submitting an invalid entry.
    """
    if not (1 <= len(PITCH) <= MAX_CHARS):
        raise SystemExit(
            f"pitch is {len(PITCH)} characters, outside the 1-{MAX_CHARS} gate"
        )
    if not PITCH.strip():
        raise SystemExit("pitch is only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"Wrote {len(PITCH)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
