#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from math import prod


def flood_basin(
    heightmap: list[list[int]],
    basin_map: dict[tuple[int, int], int],
    row: int,
    col: int,
) -> None:
    if heightmap[row][col] == 9 or (row, col) in basin_map:
        return

    neighbors: list[tuple[int, int]] = []
    if row > 0:
        neighbors.append((row - 1, col))  # up
    if row < len(heightmap) - 1:
        neighbors.append((row + 1, col))  # down
    if col > 0:
        neighbors.append((row, col - 1))  # left
    if col < len(heightmap[0]) - 1:
        neighbors.append((row, col + 1))  # right

    for n in neighbors:
        if n in basin_map:
            basin_map[(row, col)] = basin_map[n]
            break
    else:
        basin_map[(row, col)] = max(basin_map.values()) + 1 if basin_map else 0

    for n in neighbors:
        flood_basin(heightmap, basin_map, *n)


if __name__ == "__main__":
    with open("input") as f:
        heightmap: list[list[int]] = [[int(ch) for ch in line.strip()] for line in f]

    basin_map: dict[tuple[int, int], int] = {}
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            flood_basin(heightmap, basin_map, row, col)

    print(prod(b[1] for b in Counter(basin_map.values()).most_common(3)))
