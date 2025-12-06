"""Day 06 - Part 1"""
import math
from pathlib import Path
import re


OPERATIONS = {"+": sum, "*": math.prod}


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data):
    [*number_lines, operators_line] = data
    number_groups = [[]]
    for number in zip(*number_lines):
        number = "".join(number)
        if not number.strip():
            number_groups.append([])
        else:
            number_groups[-1].append(int(number))
    return sum([
        OPERATIONS[symbol](numbers)
        for numbers, symbol in zip(number_groups, operators_line.split())
    ])


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
