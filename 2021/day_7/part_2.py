#!/usr/bin/env python3

from statistics import mean


def distance(x: int, y: int) -> float:
    n: int = abs(x - y)
    return n * (n + 1) / 2


def required_fuel(pos: int, crabs: list[int]) -> int:
    return sum(distance(pos, p) for p in crabs)


if __name__ == "__main__":
    with open("input") as f:
        positions: list[int] = [int(n) for n in f.readline().strip().split(",")]

    start = int(mean(positions))
    step = (
        1
        if required_fuel(start + 1, positions) < required_fuel(start - 1, positions)
        else -1
    )

    min_fuel = required_fuel(start, positions)
    while (current_fuel := required_fuel(start + step, positions)) < min_fuel:
        min_fuel = current_fuel
        start += step

    print(min_fuel)
