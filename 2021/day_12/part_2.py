#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict


def cave_is_small(cave_name: str) -> bool:
    return cave_name.islower()


def can_visit_small_caves(visited_caves: list[str]) -> bool:
    counter = Counter(cave for cave in visited_caves if cave_is_small(cave))
    return (
        all(v < 3 for v in counter.values())
        and sum(1 for v in counter.values() if v > 1) < 2
    )


def cave_paths(
    cave: str,
    cave_map: dict[str, set[str]],
    visited_caves: list[str] | None = None,
) -> list[list[str]]:
    if visited_caves is None:
        visited_caves = []

    if (
        cave == "end"
        or (cave == "start" and visited_caves)
        or (cave_is_small(cave) and not can_visit_small_caves(visited_caves + [cave]))
    ):
        return [[cave]]

    visited_caves.append(cave)

    return [
        [cave] + path
        for neighbor in cave_map[cave]
        for path in cave_paths(neighbor, cave_map, visited_caves[:])
        if path[-1] == "end"
    ]


if __name__ == "__main__":
    cave_map: defaultdict[str, set[str]] = defaultdict(set)
    with open("input") as f:
        for line in f:
            start, end = line.strip().split("-")
            cave_map[start].add(end)
            cave_map[end].add(start)

    paths = cave_paths("start", cave_map)
    print(*paths, sep="\n")
    print(len(paths))
