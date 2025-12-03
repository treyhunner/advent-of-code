"""Day 03 - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(battery_banks):
    joltage = 0
    for bank in battery_banks:
        first = max(bank[:-1])
        second = max(bank[bank.index(first)+1:])
        joltage += int(first + second)
    return joltage


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
