"""Day 09 - Part 1"""
from collections import defaultdict
from dataclasses import astuple, dataclass
from itertools import combinations, pairwise
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
    (x1, y1), (x2, y2) = point1, point2
    return (abs((x2 - x1)) + 1) * (abs(y2 - y1) + 1)


def segment_range(a, b, exclude=False):
    a, b = sorted((a, b))
    if exclude:
        return range(a+1, b)
    else:
        return range(a, b+1)


def group_by(items, *, key):
    grouped = defaultdict(list)
    for item in items:
        grouped[key(item)].append(item)
    return grouped


def minmax(numbers):
    numbers = list(numbers)  # I'm lazy
    return (min(numbers), max(numbers))


def solve(data):
    reds = [
        Point(*(int(n) for n in line.split(",")))
        for line in data
    ]

    x_segments = {}
    y_segments = {}
    for p1, p2 in pairwise([*reds, reds[0]]):
        if p1.x == p2.x:
            x_segments.setdefault(p1.x, []).append(segment_range(p1.y, p2.y))
        else:
            y_segments.setdefault(p1.y, []).append(segment_range(p1.x, p2.x))

    biggest_area = 1
    for a, b in combinations(reds, 2):
        if (area := area_between(a, b)) > biggest_area:
            for x in segment_range(a.x, b.x, exclude=True):
                if any(a.y in s or b.y in s for s in x_segments.get(x, [])):
                    break
            else:
                for y in segment_range(a.y, b.y, exclude=True):
                    if any(a.x in s or b.x in s for s in y_segments.get(y, [])):
                        break
                else:
                    biggest_area = area

    return biggest_area


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
