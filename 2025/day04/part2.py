"""Day 04 - Part 2"""
from pathlib import Path

from part1 import parse_input, adjacent


def remove_rolls(data):
    accessible = 0
    for n, row in enumerate(data):
        for m, item in enumerate(row):
            if item == "@" and list(adjacent(data, n, m)).count("@") < 4:
                data[n][m] = "x"
                accessible += 1
    return accessible


def solve(data):
    data = [list(row) for row in data]
    accessible = 0
    while removed := remove_rolls(data):
        accessible += removed
    return accessible


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
