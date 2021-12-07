#!/usr/bin/env python3

from statistics import median


if __name__ == "__main__":
    with open("input") as f:
        positions: list[int] = [int(n) for n in f.readline().strip().split(",")]

    median = median(positions)
    fuel = sum(abs(p - median) for p in positions)
    print(fuel)
