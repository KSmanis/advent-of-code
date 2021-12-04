#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Board:
    @dataclass
    class Cell:
        number: int
        marked: bool = False

    grid: list[list[Cell]] = field(default_factory=list)

    def cells(self) -> list[Cell]:
        return [cell for row in self.rows() for cell in row]

    def columns(self) -> list[list[Cell]]:
        # https://stackoverflow.com/a/4937526/
        return [*zip(*self.grid)]

    def rows(self) -> list[list[Cell]]:
        return self.grid

    def mark_number(self, number: int) -> None:
        for cell in self.cells():
            if cell.number == number:
                cell.marked = True

    def bingo(self) -> bool:
        for line in self.rows() + self.columns():
            if all(cell.marked for cell in line):
                return True
        return False

    def score(self) -> int:
        return sum(cell.number for cell in self.cells() if not cell.marked)


if __name__ == "__main__":
    boards: list[Board] = []

    with open("input") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                numbers: list[int] = [int(n) for n in line.split(",")]
            elif line:
                boards[-1].grid.append([Board.Cell(int(n)) for n in line.split()])
            else:
                boards.append(Board())

    for n in numbers:
        for board in boards:
            board.mark_number(n)
            if board.bingo():
                print(n * board.score())
                exit()
