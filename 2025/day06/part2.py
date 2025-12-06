"""Day 06 - Part 1"""
import math
from pathlib import Path
import re


OPERATIONS = {"+": sum, "*": math.prod}
BLANK_RE = re.compile(r"\n *\n")


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def all_spaces(characters):
    """Return True if all characters are whitespace."""
    return all(c.isspace() for c in characters)


def parse_cephalopod_lines(lines):
    """Transpose rows into columns read right-to-left."""
    return "\n".join(reversed([
        "".join(column)
        for column in zip(*lines)
    ]))


def solve(data):
    [*number_lines, symbol_line] = data
    transposed_lines = parse_cephalopod_lines(number_lines)
    symbols = list(reversed(symbol_line.split()))
    number_groups = [
        [int(n) for n in line.split()]
        for line in BLANK_RE.split(transposed_lines)  # split by blank line
    ]
    return sum([
        OPERATIONS[symbol](numbers)
        for numbers, symbol in zip(number_groups, symbols)
    ])


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
