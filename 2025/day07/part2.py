"""Day 07 - Part 1"""
from collections import Counter
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data):
    possibilities = Counter([data[0].index("S")])
    for line in data:
        for index, char in enumerate(line):
            if char == "^" and index in possibilities:
                count = possibilities.pop(index)
                possibilities[index-1] += count
                possibilities[index+1] += count
    return possibilities.total()


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
