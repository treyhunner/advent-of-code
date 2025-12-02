"""Day 02 - Part 2"""
from pathlib import Path
import re

from part1 import parse_ranges


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text()


def solve(data):
    """Find sum of numbers with one or more repeated digit pairs."""
    repeated_digit_pair_re = re.compile(r"(\d+)\1+")
    return sum(
        n
        for n in parse_ranges(data)
        if repeated_digit_pair_re.fullmatch(str(n))
    )


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
