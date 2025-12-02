"""Day 01 - Part 2"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(turns):
    position = 50
    zeroes = 0

    for turn in turns:
        direction = turn[0]
        clicks = int(turn[1:])
        multiplier = -1 if direction == "L" else 1

        for _ in range(clicks):
            position += multiplier
            position %= 100
            if position == 0:
                zeroes += 1

    return zeroes


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
