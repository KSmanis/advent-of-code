#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass
class Octopus:
    x: int
    y: int
    energy_level: int


def simulate_flashes(octopus_map: dict[tuple[int, int], Octopus]) -> int:
    flashy_octopi: list[Octopus] = []
    for octopus in octopus_map.values():
        octopus.energy_level += 1
        if octopus.energy_level > 9:
            flashy_octopi.append(octopus)

    i: int = 0
    while i < len(flashy_octopi):
        octopus = flashy_octopi[i]
        for x, y in product({-1, 0, 1}, repeat=2):
            if (x, y) == (0, 0):
                continue

            neighbor_point = (octopus.x + x, octopus.y + y)
            if neighbor_point not in octopus_map:
                continue

            neighbor = octopus_map[neighbor_point]
            neighbor.energy_level += 1
            if neighbor.energy_level > 9 and neighbor not in flashy_octopi:
                flashy_octopi.append(neighbor)
        i += 1

    for octopus in flashy_octopi:
        octopus.energy_level = 0
    return len(flashy_octopi)


if __name__ == "__main__":
    with open("input") as f:
        octopus_map: dict[tuple[int, int], Octopus] = {
            (x, y): Octopus(x, y, int(ch))
            for x, line in enumerate(f)
            for y, ch in enumerate(line.strip())
        }

    print(sum(simulate_flashes(octopus_map) for _ in range(100)))
