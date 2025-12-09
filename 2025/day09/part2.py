"""Day 09 - Part 1"""
from collections import defaultdict
from dataclasses import astuple, dataclass
from itertools import combinations, cycle, pairwise
from pathlib import Path


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    def __iter__(self):
        return iter(astuple(self))


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def area_between(point1, point2):
    """Return area in square between 2 points."""
    (x1, y1), (x2, y2) = point1, point2
    return (abs((x2 - x1)) + 1) * (abs(y2 - y1) + 1)


def solve(data):
    reds = [
        Point(*(int(n) for n in line.split(",")))
        for line in data
    ]

    vertical_edges = []
    horizontal_edges = []
    for a, b in pairwise([*reds, reds[0]]):
        if a.x == b.x:
            y1, y2 = sorted((a.y, b.y))
            vertical_edges.append((a.x, y1, y2))
        else:
            x1, x2 = sorted((a.x, b.x))
            horizontal_edges.append((a.y, x1, x2))

    def boundaries_are_inside(a, b):
        # Chat GPT fixed the logic in this function for me
        x_low, x_high = sorted((a.x, b.x))
        y_low, y_high = sorted((a.y, b.y))
        for x_edge, y1, y2 in vertical_edges:
            if x_low < x_edge < x_high:
                if max(y_low, y1) < min(y_high, y2):
                    # Open-interval overlap in Y
                    return False
        for y_edge, x1, x2 in horizontal_edges:
            if y_low < y_edge < y_high:
                if max(x_low, x1) < min(x_high, x2):
                    # Open-interval overlap in X
                    return False

        return True

    biggest_area = 1
    for a, b in combinations(reds, 2):
        area = area_between(a, b)
        if area > biggest_area and boundaries_are_inside(a, b):
            biggest_area = area

    return biggest_area


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
