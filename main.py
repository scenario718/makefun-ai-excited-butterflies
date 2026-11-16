"""Copy the bundled butterfly eruption image to the entry output, byte for byte."""

import os
from pathlib import Path


def main() -> None:
    """Read the shipped image and write it out as entry.png."""
    here = Path(__file__).parent
    asset = here / "butterflies.jpg"

    data = asset.read_bytes()

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    target = output_dir / "entry.png"
    target.write_bytes(data)

    print(f"Wrote {len(data)} bytes to {target}")


if __name__ == "__main__":
    main()
