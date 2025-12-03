"""Day 03 - Part 2"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(battery_banks, count=12):
    joltage = 0
    for bank in battery_banks:
        batteries = []
        position = 0
        for i in range(12):
            battery = max(bank[position : len(bank)-count+i+1])
            batteries.append(battery)
            position = bank.index(battery, position) + 1
        joltage += int("".join(batteries))
    return joltage


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
