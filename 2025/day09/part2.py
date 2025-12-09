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


def segment_range(a, b, exclusive=False):
    """Return a range between two numbers."""
    a, b = sorted((a, b))
    if exclusive:
        return range(a+1, b)
    else:
        return range(a, b+1)


def crosses(n, segments):
    """Return True if n is within the (start, end) segment."""
    return any(
        n in s
        for s in segments
    )


def solve(data):
    reds = [
        Point(*(int(n) for n in line.split(",")))
        for line in data
    ]

    x_segments = defaultdict(list)
    y_segments = defaultdict(list)
    for a, b in pairwise([*reds, reds[0]]):
        if a.x == b.x:
            x_segments[a.x].append(segment_range(a.y, b.y))
        else:
            y_segments[a.y].append(segment_range(a.x, b.x))

    def boundaries_are_inside(a, b):
        for x in segment_range(a.x, b.x, exclusive=True):
            if crosses(a.y, x_segments[x]):
                return False
            if crosses(b.y, x_segments[x]):
                return False
        for y in segment_range(a.y, b.y, exclusive=True):
            if crosses(a.x, y_segments[y]):
                return False
            if crosses(b.x, y_segments[y]):
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
