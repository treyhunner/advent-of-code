"""Day 08 - Part 1"""
from itertools import combinations
from pathlib import Path
from weakref import ref

from part1 import parse_input, Point


def solve(data):
    points = [
        Point.from_string(line)
        for line in data
    ]
    distances = sorted(
        ((p-q).magnitude, p, q)
        for p, q in combinations(points, 2)
    )
    points_to_circuits = {
        p: {p}
        for p in points
    }
    unique_circuits = list(points_to_circuits.values())
    for distance, p, q in distances:
        if points_to_circuits[p] is not points_to_circuits[q]:
            circuit, to_merge = points_to_circuits[p], points_to_circuits[q]
            points_to_circuits[p] |= to_merge
            points_to_circuits |= dict.fromkeys(to_merge, circuit)
            unique_circuits.remove(to_merge)
        if len(unique_circuits) == 1:
            return p.x * q.x


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
