"""Write the one-line pitch to /output/entry.txt (or MAKEFUN_OUTPUT_DIR)."""

import os
import sys
from pathlib import Path

TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"
    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
