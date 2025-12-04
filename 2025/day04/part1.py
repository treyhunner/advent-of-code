"""Day 04 - Part 1"""
from collections import deque
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def adjacent(grid, x, y):
    """Return the (up to 8) cells adjacent to (x, y)."""
    items = []
    before_y, after_y = max(y-1, 0), y+2
    if x > 0:
        items.extend(grid[x-1][before_y:after_y])
    if y > 0:
        items.append(grid[x][y-1])
    if y < len(grid[x]) - 1:
        items.append(grid[x][y+1])
    if x < len(grid) - 1:
        items.extend(grid[x+1][before_y:after_y])
    return items


def solve(data):
    accessible = 0
    for n, row in enumerate(data):
        for m, item in enumerate(row):
            if item == "@" and adjacent(data, n, m).count("@") < 4:
                accessible += 1
    return accessible


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
