#!/usr/bin/env python3
from __future__ import annotations

CHUNK_PAIRS: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
REVERSE_CHUNK_PAIRS: dict[str, str] = {v: k for k, v in CHUNK_PAIRS.items()}
CHUNK_ERROR_SCORES: dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


class ChunkError(ValueError):
    def __init__(self, chunk):
        self.chunk = chunk
        self.score = CHUNK_ERROR_SCORES[chunk]


def parse_chunks(line: str) -> list[str]:
    chunks: list[str] = []
    for ch in line:
        if ch in CHUNK_PAIRS:
            chunks.append(ch)
        elif ch in REVERSE_CHUNK_PAIRS:
            if chunks.pop() != REVERSE_CHUNK_PAIRS[ch]:
                raise ChunkError(ch)
    return chunks


if __name__ == "__main__":
    syntax_error_score: int = 0
    with open("input") as f:
        for line in f:
            try:
                parse_chunks(line)
            except ChunkError as e:
                syntax_error_score += e.score

    print(syntax_error_score)
