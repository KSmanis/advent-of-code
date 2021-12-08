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

    def output(self) -> int:
        signal_map: dict[int, Digit] = {}

        for digit in self.signals - frozenset(signal_map.values()):
            if len(digit.segments) == 2:
                signal_map[1] = digit
            elif len(digit.segments) == 3:
                signal_map[7] = digit
            elif len(digit.segments) == 4:
                signal_map[4] = digit
            elif len(digit.segments) == 7:
                signal_map[8] = digit

        for digit in self.signals - frozenset(signal_map.values()):
            if digit.segments > signal_map[4].segments:
                signal_map[9] = digit
            elif len(digit.segments) == 5:
                if digit.segments > signal_map[7].segments:
                    signal_map[3] = digit
            elif len(digit.segments) == 6:
                if digit.segments > signal_map[1].segments:
                    signal_map[0] = digit
                else:
                    signal_map[6] = digit

        for digit in self.signals - frozenset(signal_map.values()):
            if signal_map[6].segments > digit.segments:
                signal_map[5] = digit
            else:
                signal_map[2] = digit

        reverse_signal_map = {v: k for k, v in signal_map.items()}
        return int("".join(str(reverse_signal_map[digit]) for digit in self.outputs))


if __name__ == "__main__":
    with open("input") as f:
        entries: list[Entry] = [Entry.from_str(line) for line in f]

    print(sum(e.output() for e in entries))
