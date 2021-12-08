#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Digit:
    segments: frozenset[str]

    @classmethod
    def from_str(cls, digit: str) -> Digit:
        return cls(segments=frozenset(digit))


@dataclass(frozen=True)
class Entry:
    signals: frozenset[Digit]
    outputs: tuple[Digit]

    @classmethod
    def from_str(cls, entry: str) -> Entry:
        tokens = entry.split(" | ")
        return cls(
            signals=frozenset(Digit.from_str(digit) for digit in tokens[0].split()),
            outputs=tuple(Digit.from_str(digit) for digit in tokens[1].split()),
        )


if __name__ == "__main__":
    with open("input") as f:
        entries: list[Entry] = [Entry.from_str(line) for line in f]

    print(sum(1 for e in entries for o in e.outputs if len(o.segments) in (2, 3, 4, 7)))
