#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter

if __name__ == "__main__":
    counters: list[Counter] = []

    with open("input") as f:
        for line in f:
            number = line.strip()
            for i, digit in enumerate(number):
                if len(counters) <= i:
                    counters.append(Counter())
                counters[i][digit] += 1

    gamma_rate = int("".join(counter.most_common()[0][0] for counter in counters), 2)
    epsilon_rate = int("".join(counter.most_common()[1][0] for counter in counters), 2)
    print(gamma_rate * epsilon_rate)
