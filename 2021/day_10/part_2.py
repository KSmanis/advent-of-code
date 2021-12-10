#!/usr/bin/env python3
from __future__ import annotations

from statistics import median

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
CHUNK_AUTOCOMPLETE_SCORES: dict[str, int] = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
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


def autocomplete_score(chunks: list[str]) -> int:
    score: int = 0
    for chunk in chunks:
        score *= 5
        score += CHUNK_AUTOCOMPLETE_SCORES[chunk]
    return score


if __name__ == "__main__":
    autocomplete_scores: list[int] = []
    with open("input") as f:
        for line in f:
            try:
                chunks = parse_chunks(line)
                missing_chunks = [CHUNK_PAIRS[chunk] for chunk in reversed(chunks)]
                autocomplete_scores.append(autocomplete_score(missing_chunks))
            except ChunkError:
                pass

    print(median(autocomplete_scores))
