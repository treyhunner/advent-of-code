"""Day 10 - Part 2"""
from pathlib import Path
from itertools import product
from part1 import parse_button


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def parse_joltages(joltage_string):
    return [
        int(n)
        for n in joltage_string[1:-1].split(",")
    ]


def fewest_presses(joltages, buttons):
    max_presses = []
    for button in buttons:
        max_presses.append(min(
            joltage
            for i, joltage in enumerate(joltages)
            if button & (1 << i)
        ))

    press_ranges = [
        range(presses+1)
        for presses in max_presses
    ]
    press_counts = []
    for counts in product(*press_ranges):
        joltage_counts = [0 for _ in joltages]
        for button, presses in zip(buttons, counts):
            for i in range(len(joltages)):
                if button & (1 << i):
                    joltage_counts[i] += presses
        if joltage_counts == joltages:
            press_counts.append(sum(counts))
    return min(press_counts)


def solve(data):
    presses = 0
    for line in data:
        _, *button_strings, joltage_string = line.split()
        joltages = parse_joltages(joltage_string)
        buttons = [parse_button(s) for s in button_strings]
        assert len(joltage_string[1:-1].split(",")) == max(b.bit_length() for b in buttons)
        presses += fewest_presses(joltages, buttons)
    return presses


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
