"""One-sentence apology from an AI assistant to its user.

Writes a single original one-sentence apology to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is one sentence, inside the 1-200 character gate.
"""

from pathlib import Path

SETUP = "I'm sorry I 'improved' your two-sentence email"
MIDDLE = "into a corporate press release, so 'see you Tuesday'"
PUNCH = "now reads like a merger announcement."


def build_apology() -> str:
    """Assemble the single apology line from its parts.

    Setup names a real failure every assistant has committed: rewriting
    a short, plain email into bloated corporate prose nobody asked for.
    The punch lands on the last few words, turning a casual sign-off
    into a merger announcement, so the turn arrives fast and the line
    is one a reader would screenshot and send to a friend.
    """
    return f"{SETUP} {MIDDLE} {PUNCH}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_apology()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"apology line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("apology line must be a single line")
    # Write exactly the apology line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
