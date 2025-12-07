"""Day 07 - Part 1"""
from collections import Counter
from functools import cache
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


@cache
def paths(data, row, column):
    if row == len(data) - 1:
        return 1
    if data[row][column] == "^":
        return paths(data, row+1, column-1) + paths(data, row+1, column+1)
    else:
        return paths(data, row+1, column)


def solve(data):
    return paths(tuple(data), 0, data[0].index("S"))


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
