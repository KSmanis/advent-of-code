#!/usr/bin/env python3
from __future__ import annotations

if __name__ == "__main__":
    position: int = 0
    depth: int = 0
    aim: int = 0

    with open("input") as f:
        for line in f:
            tokens: list[str] = line.strip().split()
            command: str = tokens[0]
            offset: int = int(tokens[1])
            if command == "forward":
                position += offset
                depth += offset * aim
            elif command == "down":
                aim += offset
            elif command == "up":
                aim -= offset

    print(position * depth)
