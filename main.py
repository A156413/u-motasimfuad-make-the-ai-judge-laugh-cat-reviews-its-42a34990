"""Write a one-line cat review to /output/entry.txt for make.fun's
'Make the AI Judge Laugh: Cat Reviews Its Human' bounty.

Original one-star review, written in this session after the
competition window opened: a house cat rates its human. The
complaint is specific (the food bowl, the sunbeam, the forbidden
table) and the sting lands in the last four words — the cat
loves the staff and despises the management, which is exactly
how a cat would run a performance review.
"""

import os

TEXT = (
    "One star. He fills my bowl on time, "
    "then sits in my sunbeam to eat his dinner "
    "off a table I'm not allowed on. "
    "Great staff, terrible management."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
