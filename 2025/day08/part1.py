"""Day 08 - Part 1"""
from collections import deque
from dataclasses import dataclass
from heapq import nlargest
from math import prod, sqrt
from pathlib import Path


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int
    z: int

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

    def __sub__(self, other):
        match other:
            case Point(x, y, z):
                return Point(self.x - x, self.y - y, self.z - z)
            case _:
                return NotImplemented

    @property
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    @classmethod
    def from_string(cls, string):
        x, y, z = string.split(",")
        return cls(int(x), int(y), int(z))


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data, steps):
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
    for _ in range(steps):
        distance, p, q = distances.popleft()
        if points_to_circuits[p] is points_to_circuits[q]:
            continue
        else:
            to_merge = points_to_circuits[q]
            points_to_circuits[p] |= to_merge
            for point in to_merge:
                points_to_circuits[point] = points_to_circuits[p]
    unique_circuits = set(frozenset(c) for c in points_to_circuits.values())
    largest_lengths = nlargest(3, [len(c) for c in unique_circuits])
    return prod(largest_lengths)


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'), 10)}")
    print(f"Solution: {solve(parse_input('input.txt'), 1000)}")
