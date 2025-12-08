"""Day 08 - Part 1"""
from collections import deque
from pathlib import Path
from weakref import ref

from part1 import parse_input, Point


def solve(data):
    points = [
        Point.from_string(line)
        for line in data
    ]
    pairs = {
        frozenset((p, q)): (p-q).magnitude
        for p in points
        for q in points
        if p is not q
    }
    distances = deque(sorted(
        (distance, p, q)
        for (p, q), distance in pairs.items()
    ))
    points_to_circuits = {
        p: {p}
        for p in points
    }
    unique_circuits = [ref(c) for c in points_to_circuits.values()]
    while sum(r() is not None for r in unique_circuits) > 1:
        distance, p, q = distances.popleft()
        if points_to_circuits[p] is not points_to_circuits[q]:
            to_merge = points_to_circuits[q]
            points_to_circuits[p] |= to_merge
            circuit = points_to_circuits[p]
            points_to_circuits |= {point: circuit for point in to_merge}
            del to_merge  # delete last remaining reference
    return p.x * q.x


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
