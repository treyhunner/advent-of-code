"""Day 11 - Part 2"""
from collections import Counter
from functools import cache
from math import prod
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def next_devices(devices, current_devices):
    for device in current_devices:
        yield from devices.get(device, [])


def steps_from(devices, start, end):
    steps = [step := {start}]
    while step:
        steps.append(step := set(next_devices(devices, steps[-1])))
    step_options = {
        count: steps[:count]
        for count, step in enumerate(steps, start=1)
        if end in step
    }
    if not step_options:
        raise ValueError("No valid paths")
    return step_options


def solve(data):
    forward = {}
    backward = {}
    for line in data:
        device, outputs = line.split(":")
        forward[device] = outputs.split()
        for to_device in forward[device]:
            backward.setdefault(to_device, set()).add(device)

    def paths_between(start, end):
        step_options_there = steps_from(forward, start, end)
        step_options_back = steps_from(backward, end, start)
        paths = 0
        for count, steps_there in step_options_there.items():
            steps_back = step_options_back[count]
            paths += prod(
                len(there & back)
                for there, back in zip(steps_there, reversed(steps_back))
            )
        return paths

    return (
        paths_between("svr", "fft") *
        paths_between("fft", "dac") *
        paths_between("dac", "out")
    )


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample2.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
