#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import cycle


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, point: str) -> Point:
        return cls(*map(int, point.split(",")))


@dataclass(frozen=True)
class Line:
    start: Point
    end: Point

    @classmethod
    def from_str(cls, line: str) -> Line:
        return cls(*map(Point.from_str, line.split(" -> ")))

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def points(self) -> list[Point]:
        x_step = 1 if self.end.x >= self.start.x else -1
        y_step = 1 if self.end.y >= self.start.y else -1
        x_range = range(self.start.x, self.end.x + x_step, x_step)
        y_range = range(self.start.y, self.end.y + y_step, y_step)
        if self.is_horizontal():
            y_range = cycle(y_range)
        elif self.is_vertical():
            x_range = cycle(x_range)
        return [Point(x, y) for x, y in zip(x_range, y_range)]


if __name__ == "__main__":
    vent_map: Counter[Point] = Counter()

    with open("input") as f:
        for line in f:
            vent = Line.from_str(line.strip())
            for point in vent.points():
                vent_map[point] += 1

    print(len([v for v in vent_map.values() if v >= 2]))
