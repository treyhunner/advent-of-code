"""Day 10 - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def parse_lights(light_string):
    lights = [c == "#" for c in light_string[1:-1]]
    bitmask = 0
    for i, on in enumerate(lights):
        bitmask ^= on << i
    return bitmask


def parse_button(button_string):
    light_indexes = [int(n) for n in button_string[1:-1].split(",")]
    bitmask = 0
    for light in light_indexes:
        bitmask ^= 1 << light
    return bitmask


def fewest_presses(lights, buttons):
    press_counts = []
    for combination in range(2 ** len(buttons)):
        button_mask = 0
        for i, button in enumerate(buttons):
            if combination & (1 << i):
                button_mask ^= button
        if lights == button_mask:
            press_counts.append(combination.bit_count())
    return min(press_counts)


def solve(data):
    presses = 0
    for line in data:
        light_string, *button_strings, joltage = line.split()
        lights = parse_lights(light_string)
        buttons = [parse_button(s) for s in button_strings]
        assert len(light_string[1:-1]) == max(b.bit_length() for b in buttons)
        presses += fewest_presses(lights, buttons)
    return presses


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
