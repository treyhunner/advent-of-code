"""Day 08 - Part 1"""
from collections import deque
from pathlib import Path

from part1 import parse_input, Point


def solve(data):
    points = [
        Point.from_string(line)
        for line in data
    ]
    pairs = {}
    for p in points:
        for q in points:
            pairs[tuple(sorted([p, q]))] = (p-q).magnitude
    distances = deque(sorted(
        (distance, p, q)
        for (p, q), distance in pairs.items()
        if p is not q
    ))
    points_to_circuits = {
        p: {p}
        for p in points
    }
    unique_circuits = set(id(c) for c in points_to_circuits.values())
    while len(unique_circuits) > 1:
        distance, p, q = distances.popleft()
        if points_to_circuits[p] is points_to_circuits[q]:
            continue
        else:
            to_merge = points_to_circuits[q]
            points_to_circuits[p] |= to_merge
            for point in to_merge:
                points_to_circuits[point] = points_to_circuits[p]
            unique_circuits.remove(id(to_merge))
    return p.x * q.x


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
