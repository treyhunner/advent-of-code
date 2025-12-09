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


def points_between(point1, point2):
    """Return points between two points (they share a common coordinate)."""
    (x1, y1), (x2, y2) = point1, point2
    if x1 == x2:
        a, b = sorted((y1, y2))
        return [Point(x1, y) for y in range(a+1, b)]
    else:
        a, b = sorted((x1, x2))
        return [Point(x, y1) for x in range(a+1, b)]


def segment_range(a, b):
    """Return a range between (and including) two numbers."""
    a, b = sorted((a, b))
    return range(a, b+1)


def is_inside(n, segments):
    """Return True if n is within the (start, end) segment."""
    return any(
        start <= n <= end
        for start, end in segments
    )


def edges_only(points, axis):
    """
    Return only the edge points in a given x/y direction.

    A point is an edge if it is not sandwiched between 2 other points.
    """
    edges = [points[0]]
    for previous, point in pairwise(points):
        if getattr(point, axis) != getattr(previous, axis) + 1:
            edges.append(point)
    if edges[-1] != point:
        edges.append(point)
    return edges


def group_by(items, *, key):
    """Group items into a dictionary by a given key funcion."""
    grouped = defaultdict(list)
    for item in items:
        grouped[key(item)].append(item)
    return grouped


def solve(data):
    reds = [
        Point(*(int(n) for n in line.split(",")))
        for line in data
    ]

    greens = []
    for p1, p2 in pairwise([*reds, reds[0]]):
        greens += points_between(p1, p2)

    reds_and_greens = reds + greens

    points_by_x = group_by(reds_and_greens, key=lambda p: p.x)
    segments_inside_x = {}
    for x, points in points_by_x.items():
        points.sort(key=lambda p: p.y)
        segments = segments_inside_x[x] = []
        inside = True
        for p, q in pairwise(edges_only(points, "y")):
            if inside:
                segments.append((p.y, q.y))
            inside = not inside

    points_by_y = group_by(reds_and_greens, key=lambda p: p.y)
    segments_inside_y = defaultdict(list)
    for y, points in points_by_y.items():
        points.sort(key=lambda p: p.x)
        segments = segments_inside_y[y] = []
        inside = True
        for p, q in pairwise(edges_only(points, "x")):
            if inside:
                segments.append((p.x, q.x))
            inside = not inside

    def boundaries_are_inside(a, b):
        for x in segment_range(a.x, b.x):
            if not is_inside(a.y, segments_inside_x[x]):
                return False
            if not is_inside(b.y, segments_inside_x[x]):
                return False
        for y in segment_range(a.y, b.y):
            if not is_inside(a.x, segments_inside_y[y]):
                return False
            if not is_inside(b.x, segments_inside_y[y]):
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
