"""Day 11 - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def paths_from(devices, start, end):
    if start == end:
        return [[end]]
    return [
        [device, *path]
        for device in devices[start]
        for path in paths_from(devices, device, end)
    ]


def solve(data):
    devices = {}
    for line in data:
        device, outputs = line.split(":")
        devices[device] = outputs.split()
    return len(paths_from(devices, "you", "out"))


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
