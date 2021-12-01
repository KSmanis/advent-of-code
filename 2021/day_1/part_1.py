#!/usr/bin/env python3
from __future__ import annotations

if __name__ == "__main__":
    count: int = 0
    prev: int = 0

    with open("input") as f:
        for i, line in enumerate(f):
            curr: int = int(line.strip())
            if i > 0 and curr > prev:
                count += 1
            prev = curr

    print(count)
