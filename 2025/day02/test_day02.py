"""Tests for Day 02"""
import unittest
from part1 import solve as solve_part1, parse_input
from part2 import solve as solve_part2


class TestDay02(unittest.TestCase):
    """Test Advent of Code Day 2 solutions"""

    def test_part1_sample(self):
        data = parse_input("sample.txt")
        result = solve_part1(data)
        self.assertEqual(result, 1227775554)

    def test_part2_sample(self):
        data = parse_input("sample.txt")
        result = solve_part2(data)
        self.assertEqual(result, 4174379265)


if __name__ == "__main__":
    unittest.main()
