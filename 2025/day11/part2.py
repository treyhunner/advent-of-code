"""Day 11 - Part 2"""
from functools import cache
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data):
    devices = {}
    for line in data:
        device, outputs = line.split(":")
        devices[device] = outputs.split()

    @cache
    def paths_from(start, end):
        if start == end:
            return [[end]]
        return [
            [device, *path]
            for device in devices[start]
            for path in paths_from(device, end)
        ]

    return len([
        path
        for path in paths_from("svr", "out")
        if "dac" in path and "fft" in path
    ])


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample2.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
