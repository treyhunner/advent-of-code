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
    def paths_between(start, end):
        if start == end: return 1
        return sum(
            paths_between(device, end)
            for device in devices.get(start, [])
        )

    dac_to_fft = (
        paths_between("svr", "dac") *
        paths_between("dac", "fft") *
        paths_between("fft", "out")
    )  # This one is always 0
    fft_to_dac = (
        paths_between("svr", "fft") *
        paths_between("fft", "dac") *
        paths_between("dac", "out")
    )
    return dac_to_fft + fft_to_dac


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample2.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
