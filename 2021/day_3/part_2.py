#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter

if __name__ == "__main__":
    with open("input") as f:
        numbers: list[str] = f.readlines()

    oxygen_generator_numbers: list[str] = [n for n in numbers]
    co2_scrubber_numbers: list[str] = [n for n in numbers]

    i: int = 0
    while len(oxygen_generator_numbers) > 1:
        counter: Counter = Counter(n[i] for n in oxygen_generator_numbers)
        prevalent_digit: str = (
            counter.most_common()[0][0]
            if counter.most_common()[0][1] != counter.most_common()[1][1]
            else "1"
        )
        oxygen_generator_numbers = [
            n for n in oxygen_generator_numbers if n[i] == prevalent_digit
        ]
        i += 1
    oxygen_generator_rating: int = int(oxygen_generator_numbers[0], 2)

    i: int = 0
    while len(co2_scrubber_numbers) > 1:
        counter: Counter = Counter(n[i] for n in co2_scrubber_numbers)
        prevalent_digit: str = (
            counter.most_common()[1][0]
            if counter.most_common()[0][1] != counter.most_common()[1][1]
            else "0"
        )
        co2_scrubber_numbers = [
            n for n in co2_scrubber_numbers if n[i] == prevalent_digit
        ]
        i += 1
    co2_scrubber_rating: int = int(co2_scrubber_numbers[0], 2)

    print(oxygen_generator_rating * co2_scrubber_rating)
