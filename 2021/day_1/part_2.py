#!/usr/bin/env python3
from __future__ import annotations

WINDOW_OFFSET: int = 1
WINDOW_SIZE: int = 3

if __name__ == "__main__":
    count: int = 0
    window: list[int] = []

    with open("input") as f:
        for line in f:
            window.append(int(line.strip()))
            if len(window) > WINDOW_SIZE:
                if sum(window[WINDOW_OFFSET:]) > sum(window[:WINDOW_SIZE]):
                    count += 1
                window.pop(0)

    print(count)
