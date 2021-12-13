#!/usr/bin/env python3
from __future__ import annotations

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def fold_horizontally(paper: set[Point], line: int) -> set[Point]:
    added_points: set[Point] = set()
    removed_points: set[Point] = set()
    for point in paper:
        if point.y < line:
            continue
        elif point.y == line:
            removed_points.add(point)
        else:
            added_points.add(Point(point.x, 2 * line - point.y))
            removed_points.add(point)
    return paper.union(added_points).difference(removed_points)


def fold_vertically(paper: set[Point], line: int) -> set[Point]:
    added_points: set[Point] = set()
    removed_points: set[Point] = set()
    for point in paper:
        if point.x < line:
            continue
        elif point.x == line:
            removed_points.add(point)
        else:
            added_points.add(Point(2 * line - point.x, point.y))
            removed_points.add(point)
    return paper.union(added_points).difference(removed_points)


if __name__ == "__main__":
    paper: set[Point] = set()
    with open("input") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith("fold"):
                axis, line = line.split()[-1].split("=")
                if axis == "x":
                    paper = fold_vertically(paper, int(line))
                elif axis == "y":
                    paper = fold_horizontally(paper, int(line))
            else:
                paper.add(Point(*map(int, line.split(","))))

    max_x = max(point.x for point in paper)
    max_y = max(point.y for point in paper)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print("*" if Point(x, y) in paper else " ", end="")
        print()
