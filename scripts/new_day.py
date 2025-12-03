#!/usr/bin/env python3
"""Script to create a new day's directory structure."""

import sys
from pathlib import Path


PART1_TEMPLATE = '''"""Day {day:02d} - Part 1"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data):
    # TODO: Implement solution
    pass


if __name__ == "__main__":
    print(f"Sample: {{solve(parse_input('sample.txt'))}}")
    print(f"Solution: {{solve(parse_input('input.txt'))}}")
'''

PART2_TEMPLATE = '''"""Day {day:02d} - Part 2"""
from pathlib import Path


def parse_input(filename):
    return (Path(__file__).parent / filename).read_text().splitlines()


def solve(data):
    # TODO: Implement solution
    pass


if __name__ == "__main__":
    print(f"Sample: {{solve(parse_input('sample.txt'))}}")
    print(f"Solution: {{solve(parse_input('input.txt'))}}")
'''

TEST_TEMPLATE = '''"""Tests for Day {day:02d}"""
import unittest
from part1 import solve as solve_part1, parse_input
from part2 import solve as solve_part2


class TestDay{day:02d}(unittest.TestCase):
    """Test Advent of Code Day {day} solutions"""

    def test_part1_sample(self):
        data = parse_input("sample.txt")
        result = solve_part1(data)
        # self.assertEqual(result, expected_value)

    def test_part2_sample(self):
        data = parse_input("sample.txt")
        result = solve_part2(data)
        # self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
'''

README_TEMPLATE = '''# Day {day:02d}: {title}

[Link to puzzle](https://adventofcode.com/2025/day/{day})

[Notes about the solution]
'''


def find_next_day(year: int = 2025) -> int:
    """Find the next day number by looking at existing day directories."""
    year_dir = Path(f"{year}")
    if not year_dir.exists():
        return 1

    existing_days = []
    for day_dir in year_dir.glob("day*"):
        if day_dir.is_dir():
            try:
                day_num = int(day_dir.name[3:])  # Extract number from "dayXX"
                existing_days.append(day_num)
            except ValueError:
                continue

    if not existing_days:
        return 1

    return max(existing_days) + 1


def create_day(day: int, title: str, year: int = 2025):
    """Create directory structure for a new day."""
    # Create day directory
    day_dir = Path(f"{year}/day{day:02d}")
    day_dir.mkdir(parents=True, exist_ok=True)

    # Create files
    (day_dir / "__init__.py").write_text("")
    (day_dir / "part1.py").write_text(PART1_TEMPLATE.format(day=day))
    (day_dir / "part2.py").write_text(PART2_TEMPLATE.format(day=day))
    (day_dir / "test_day{:02d}.py".format(day)).write_text(TEST_TEMPLATE.format(day=day))
    (day_dir / "sample.txt").write_text("")
    (day_dir / "input.txt").write_text("")
    (day_dir / "README.md").write_text(README_TEMPLATE.format(day=day, title=title))

    print(f"Created structure for day {day:02d} at {day_dir}")
    print(f"\nNext steps:")
    print(f"1. Visit https://adventofcode.com/2025/day/{day}")
    print(f"2. Copy sample input to {day_dir}/sample.txt")
    print(f"3. Copy your puzzle input to {day_dir}/input.txt")
    print(f"4. Start coding in part1.py!")


if __name__ == "__main__":
    # Determine day number
    if len(sys.argv) > 2:
        sys.exit("Usage: python scripts/new_day.py [day_number]")

    if len(sys.argv) == 2:
        try:
            day = int(sys.argv[1])
            if not 1 <= day <= 25:
                sys.exit("Day must be between 1 and 25")
        except ValueError:
            sys.exit("Day must be a number")
    else:
        # Auto-detect next day
        day = find_next_day()
        if day > 25:
            sys.exit("All 25 days already exist!")
        print(f"Auto-detected next day: {day}")

    # Prompt for puzzle title
    title = input(f"Enter puzzle title for Day {day:02d}: ").strip()
    if not title:
        title = "[Puzzle Title]"

    create_day(day, title)
