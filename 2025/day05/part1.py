"""Day 05 - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text()


def parse_ranges(ranges):
    """Parse range lines into range objects."""
    return [
        range(int(start), int(end) + 1)
        for group in ranges.splitlines()
        for start, end in [group.split("-")]
    ]


def solve(data):
    range_lines, available_lines = data.split("\n\n")
    fresh_ranges = parse_ranges(range_lines)
    available_ids = {
        int(n)
        for n in available_lines.splitlines()
    }

    # The count of available item IDs that are fresh
    return sum(
        any(id_ in range_ for range_ in fresh_ranges)
        for id_ in available_ids
    )


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
