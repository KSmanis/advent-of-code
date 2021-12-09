#!/usr/bin/env python3
from __future__ import annotations

if __name__ == "__main__":
    with open("input") as f:
        heightmap: list[list[int]] = [[int(ch) for ch in line.strip()] for line in f]

    risk: int = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            neighbors: list[int] = []
            if row > 0:
                neighbors.append(heightmap[row - 1][col])  # up
            if row < len(heightmap) - 1:
                neighbors.append(heightmap[row + 1][col])  # down
            if col > 0:
                neighbors.append(heightmap[row][col - 1])  # left
            if col < len(heightmap[0]) - 1:
                neighbors.append(heightmap[row][col + 1])  # right

            if all(heightmap[row][col] < n for n in neighbors):
                risk += heightmap[row][col] + 1

    print(risk)
