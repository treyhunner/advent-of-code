"""Tests for Day 11"""
import unittest
from part1 import solve as solve_part1, parse_input
from part2 import solve as solve_part2


class TestDay11(unittest.TestCase):
    """Test Advent of Code Day 11 solutions"""

    def test_part1_sample(self):
        data = parse_input("sample.txt")
        result = solve_part1(data)
        self.assertEqual(result, 5)

    def test_part2_sample(self):
        data = parse_input("sample2.txt")
        result = solve_part2(data)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
