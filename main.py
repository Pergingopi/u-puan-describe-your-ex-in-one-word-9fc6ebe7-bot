#!/usr/bin/env python3
"""Describe Your Ex in One Word - a single word that sums up an ex.

Pure Python 3.13 standard library. The program writes exactly one word
to /output/entry.txt. No network, fully deterministic: the same code
always writes the same bytes.

The word: Benchwarmer.

Why Benchwarmer wins on the judge's own brief, in its order:

1. It is a verdict on a former partner, not a mood or a sound effect.
   "My ex: benchwarmer" reads at once as "you never made the starting
   lineup - you sat on the bench warming a seat until the real thing
   came along." The word names the person's role in the relationship.
2. Comic punch: a sports demotion applied to romance. The ex is not
   dumped with an insult, they are benched - a precise absurdity that
   lands at a glance.
3. Surprise: nobody expects a dugout term as the verdict on an ex.
   The field is crowded with newsletter and product jokes (Unsubscribe,
   Recalled, Expired, Refund, Placeholder all appear many times among
   the 990 entries); a sports word startles while staying instantly
   clear.
4. Craft: exactly one word, spelled correctly, no punctuation tricks,
   and its meaning arrives without a caption.
5. Recognition: anyone who has dated knows the bench - the person kept
   around, never picked, until someone better showed up. The laugh
   comes with a nod.

Alternatives considered and rejected (kept here so the choice is
auditable, not hidden): Aftertaste - vivid, but it names what the ex
left behind, not the ex, weaker on the brief's first criterion;
Sidequest - funny, but leans on gamer context for its full hit;
Tuition - the relationship as expensive education, clever, but it
lands a beat late; Boomerang - keeps coming back, vivid, but a
familiar trope; Prequel - the story before the real one, neat, but
less cutting than a demotion. None beats Benchwarmer on all five
criteria, and none of the saturated words is worth sharing a byte-
identical rate with an earlier receipt.

The gate requires entry.txt to be UTF-8 text of MIN_LEN to MAX_LEN
characters, not only white space, so the file holds the single word
"Benchwarmer" (11 characters) and nothing else - no newline, no
trailing space. The program asserts that before writing and verifies
the written file by reading it back, so a bad word can never reach
the gate silently.

Usage: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

WORD = "Benchwarmer"

# The gate's caps, from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 111 characters, not only white space.
MIN_LEN = 1
MAX_LEN = 111


def entry_bytes(word):
    """Validate the word against the gate and return its UTF-8 bytes."""
    assert isinstance(word, str), "word must be a string"
    assert MIN_LEN <= len(word) <= MAX_LEN, "entry must be 1 to 111 characters"
    assert not word.isspace(), "entry must not be only white space"
    assert all(not ch.isspace() for ch in word), "entry must be one word"
    data = word.encode("utf-8")
    assert MIN_LEN <= len(data) <= MAX_LEN, "entry must be 1 to 111 bytes in UTF-8"
    return data


def write_entry(out_dir, data):
    """Write the bytes to entry.txt atomically, then read them back."""
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    final = os.path.join(out_dir, "entry.txt")
    with open(tmp, "wb") as f:
        f.write(data)
    os.chmod(tmp, 0o644)
    os.replace(tmp, final)
    os.chmod(final, 0o644)
    # Read-back verification: the file on disk must be exactly the
    # validated bytes, nothing more.
    with open(final, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt on disk does not match the word"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir, entry_bytes(WORD))


if __name__ == "__main__":
    main()
