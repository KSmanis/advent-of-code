#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from itertools import pairwise


def polymerize(template: Counter[str], rules: dict[str, str]) -> Counter[str]:
    polymer: Counter[str] = Counter()
    for k, v in template.items():
        if k in rules:
            polymer[k[0] + rules[k]] += v
            polymer[rules[k] + k[1]] += v
    return polymer


if __name__ == "__main__":
    rules: dict[str, str] = {}
    with open("input") as f:
        template = f.readline().strip()
        for line in f:
            line = line.strip()
            if line:
                pair, element = line.split(" -> ")
                rules[pair] = element

    pair_counter: Counter[str] = Counter(a + b for a, b in pairwise(template))
    for _ in range(40):
        pair_counter = polymerize(pair_counter, rules)

    element_counter: Counter[str] = Counter()
    for k, v in pair_counter.items():
        element_counter[k[0]] += v // 2
        element_counter[k[1]] += v // 2
    print(element_counter.most_common()[0][1] - element_counter.most_common()[-1][1])
