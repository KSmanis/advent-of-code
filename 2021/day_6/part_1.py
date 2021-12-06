#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter


def simulate_day(population: Counter[int]) -> Counter[int]:
    new_population: Counter[int] = Counter()
    for k, v in population.items():
        if k > 0:
            new_population[k - 1] += v
        else:
            new_population[6] += v
            new_population[8] += v
    return new_population


if __name__ == "__main__":
    with open("input") as f:
        population: Counter[int] = Counter(
            int(n) for n in f.readline().strip().split(",")
        )

    for _ in range(80):
        population = simulate_day(population)

    print(sum(population.values()))
