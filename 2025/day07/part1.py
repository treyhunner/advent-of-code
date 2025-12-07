"""Day 07 - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data):
    beam_indexes = {data[0].index("S")}
    splits = 0
    for line in data:
        for index, char in enumerate(line):
            if char == "^" and index in beam_indexes:
                beam_indexes.remove(index)
                beam_indexes.add(index-1)
                beam_indexes.add(index+1)
                splits += 1
    return splits


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
