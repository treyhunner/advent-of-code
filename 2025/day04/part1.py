"""Day 04 - Part 1"""
from collections import deque
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def adjacent(grid, x, y):
    if x > 0:
        yield from grid[x-1][max(y-1, 0):y+2]
    if y > 0:
        yield grid[x][y-1]
    if y < len(grid[x]) - 1:
        yield grid[x][y+1]
    if x < len(grid) - 1:
        yield from grid[x+1][max(y-1, 0):y+2]


def solve(data):
    accessible = 0
    for n, row in enumerate(data):
        for m, item in enumerate(row):
            if item == "@" and list(adjacent(data, n, m)).count("@") < 4:
                accessible += 1
    return accessible


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
