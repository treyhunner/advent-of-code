"""Day 06 - Part 1"""
from itertools import groupby
import math
from pathlib import Path
import re


OPERATIONS = {"+": sum, "*": math.prod}


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def all_spaces(characters):
    """Return True if all characters are whitespace."""
    return all(c.isspace() for c in characters)


def parse_cephalopod_numbers(number_lines):
    """Return groups of number columns, separated by full space column."""
    return [
        [int("".join(digits)) for digits in chars]
        for is_whitespace, chars in groupby(zip(*number_lines), key=all_spaces)
        if not is_whitespace
    ]


def solve(data):
    [*number_lines, operators_line] = data
    symbols = operators_line.split()
    number_groups = parse_cephalopod_numbers(number_lines)
    return sum([
        OPERATIONS[symbol](numbers)
        for numbers, symbol in zip(number_groups, symbols)
    ])


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
