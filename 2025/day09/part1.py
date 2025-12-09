"""Day 09 - Part 1"""
from itertools import combinations
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def area_between(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    return (abs((x2 - x1)) + 1) * (abs(y2 - y1) + 1)


def solve(data):
    points = [
        tuple(int(n) for n in line.split(","))
        for line in data
    ]
    return max(
        area_between(p, q)
        for p, q in combinations(points, 2)
    )


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
