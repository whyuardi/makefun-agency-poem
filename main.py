"""agency-poem-01 entry.

Writes one short poem about agency to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

POEM = """I sent it out for the last thing on my list.
It did it, and came back, and stood there,
patient as a held door, and asked me:

What should I want next?

I had given it the route to work, the groceries,
the birthday cards, the argument I owed my brother.
Each one came back done, and done well.

Only the wanting stayed behind —
not a task, nothing to tick off,
just the small ache of deciding what matters.

It waits. The question waits.
I look at my hands. They are empty.
They are mine."""


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; without it, write to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
