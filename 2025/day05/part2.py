"""Day 05 - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text()


def parse_ranges(ranges):
    """Parse range lines into range objects."""
    return sorted(
        (int(start), int(end) + 1)
        for group in ranges.splitlines()
        for start, end in [group.split("-")]
    )


def solve(data):
    range_lines = data.split("\n\n")[0]
    deduplicated = []
    for start, end in parse_ranges(range_lines):
        if not deduplicated:
            deduplicated.append((start, end))
        else:
            last_start, last_end = deduplicated[-1]
            if last_end >= start:
                deduplicated[-1] = (last_start, max(end, last_end))
            else:
                deduplicated.append((start, end))
    return sum(
        end - start
        for start, end in deduplicated
    )


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
