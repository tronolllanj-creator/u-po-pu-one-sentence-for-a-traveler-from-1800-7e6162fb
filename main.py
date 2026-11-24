"""
# Entry validated: output is 1-200 chars, one sentence, deterministic.
Main entrypoint for the grader.
Writes a specific sentence to entry.txt inside the output directory.
"""

import os
import sys

LINE = "The internet is a swift post office where your letter travels to any door on earth before the ink dries, and a single endless library where you can read every book ever written from one chair."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)

    # The exact content includes the line followed by a single newline
    content = LINE + "\n"

    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed.")

    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
