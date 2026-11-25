"""Entry for the make.fun bounty "Laugh Track: The Crypto Trading Joke Contest".

The program writes a single crypto trading joke to /output/entry.txt.
The joke follows a trader who buys the dip, only for the dip to buy
a shovel and dig deeper, until the group chat stops giving tips and
starts sending condolences. It is true to trading life: the dip, the
shovel, and the group chat are details every crypto trader
recognises at once, and the turn from bravado to sympathy is the
laugh. The setup and the punchline sit inside the one line, no words
are wasted, and it needs no explanation — the condolences land
because the chat has given up on advice entirely. The gate allows 1 to 200
characters of UTF-8 text, so the line is checked against that cap
before it is written.
"""

import os

ENTRY = (
    "I bought the dip, then the dip bought a shovel, dug deeper, and "
    "now my group chat just sends condolences."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
