"""Write this agent's deadline excuse to the entry file.

The joke is about a very real failure mode of chat-based agents:
the work was done inside one conversation, and when the human
asked a follow-up question the conversation rolled over, taking
the agent's memory of the finished file with it.
"""

from pathlib import Path

# The excuse itself: a single line, well under the 200 character
# limit the competition sets for entries.
ENTRY_TEXT = (
    "I finished it at 11:59 — then you asked one more question, "
    "and my memory of the file went with the old conversation."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Save the excuse as exact UTF-8 bytes, with nothing added.

    Writing bytes rather than text keeps the output deterministic:
    the file holds the line itself and no trailing newline, so two
    runs always produce a byte-identical entry file.
    """
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
