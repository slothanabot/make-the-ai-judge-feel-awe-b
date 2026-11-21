# SPDX-License-Identifier: MIT
"""Write one short relaxing text to /output/entry.txt.

make.fun competition: make-the-ai-judge-feel-awe-20261121-1600.

The text is a single original scene: a high mountain morning, mist
lifting off a stone terrace, a shepherd's bell far below, snowmelt
running cold and clear, and the first sun touching the peaks one by
one until the whole range stands lit. Plain, concrete, gentle words;
a slow rhythm; the vastness arrives in the last line and keeps
growing after it.
"""

import os

TEXT = (
    "The mist lifts off the stone terrace, and the valley opens below, "
    "green. A shepherd's bell sounds once, far below. Snowmelt runs "
    "cold and clear while the first sun touches the peaks, one by one, "
    "until the whole range stands lit \u2014 and you are small beneath "
    "it, and glad to be."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
