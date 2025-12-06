"""Day 06 - Part 1"""
import math
from pathlib import Path


def parse_input(filename):
    path = Path(__file__).parent / filename
    return [
        line.split()
        for line in path.read_text().splitlines()
    ]


def solve(data):
    functions = {"+": sum, "*": math.prod}
    answers = []
    for [*numbers, operation] in zip(*data):
        answers.append(functions[operation](int(n) for n in numbers))
    return sum(answers)


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
