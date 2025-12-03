"""Tests for Day 03"""
import unittest
from part1 import solve as solve_part1, parse_input
from part2 import solve as solve_part2


class TestDay03(unittest.TestCase):
    """Test Advent of Code Day 3 solutions"""

    def test_part1_sample(self):
        data = parse_input("sample.txt")
        result = solve_part1(data)
        self.assertEqual(result, 357)

    def test_part2_sample(self):
        data = parse_input("sample.txt")
        result = solve_part2(data)
        self.assertEqual(result, 3121910778619)


if __name__ == "__main__":
    unittest.main()
