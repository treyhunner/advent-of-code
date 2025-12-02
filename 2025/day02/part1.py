"""Day 02 - Part 1"""
from pathlib import Path
import re


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text()


def parse_ranges(ranges):
    """Parse comma-separated ranges into sorted list of numbers."""
    return sorted(
        n
        for group in ranges.split(",")
        for start, end in [group.split("-")]
        for n in range(int(start), int(end) + 1)
    )


def solve(data):
    """Find sum of numbers with exactly one repeated digit pair."""
    repeated_digit_pair_re = re.compile(r"(\d+)\1")
    return sum(
        n
        for n in parse_ranges(data)
        if repeated_digit_pair_re.fullmatch(str(n))
    )


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
