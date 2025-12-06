"""Day 06 - Part 1"""
import math
from pathlib import Path


OPERATIONS = {"+": sum, "*": math.prod}


def parse_input(filename):
    path = Path(__file__).parent / filename
    return [
        line.split()
        for line in path.read_text().splitlines()
    ]


def solve(data):
    return sum([
        OPERATIONS[symbol](int(n) for n in numbers)
        for [*numbers, symbol] in zip(*data)
    ])


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
