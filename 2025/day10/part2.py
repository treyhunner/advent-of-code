#!/usr/bin/env uvrs
# /// script
# dependencies = [
#     "pulp",
# ]
#
# [tool.uv]
# exclude-newer = "2025-12-11T07:07:50Z"
# ///
"""Day 10 - Part 2"""
from pathlib import Path

from pulp import LpProblem, LpMinimize, LpInteger, LpVariable, lpSum, PULP_CBC_CMD

from part1 import parse_button


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def parse_joltages(joltage_string):
    return [
        int(n)
        for n in joltage_string[1:-1].split(",")
    ]


def fewest_presses(joltages, buttons):
    model = LpProblem("joltage", LpMinimize)  # We're minimizing presses

    # Variables: presses for each button (non-negative integers)
    press_variables = [
        LpVariable(f"button{i}", lowBound=0, cat=LpInteger)
        for i in range(len(buttons))
    ]

    # Constraints: for each joltage
    for i, joltage in enumerate(joltages):
        model += lpSum(
            variable * bool(button & (1 << i))
            for variable, button in zip(press_variables, buttons)
        ) == joltage

    # Objectives: minimize total button presses
    model += lpSum(press_variables)

    model.solve(PULP_CBC_CMD(msg=False))
    return int(sum(v.value() for v in press_variables))


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
