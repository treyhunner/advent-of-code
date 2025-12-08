"""Tests for Day 08"""
import unittest
from part1 import solve as solve_part1, parse_input
from part2 import solve as solve_part2


class TestDay08(unittest.TestCase):
    """Test Advent of Code Day 8 solutions"""

    def test_part1_sample(self):
        data = parse_input("sample.txt")
        result = solve_part1(data, 10)
        self.assertEqual(result, 40)

    def test_part2_sample(self):
        data = parse_input("sample.txt")
        result = solve_part2(data)
        self.assertEqual(result, 25272)


if __name__ == "__main__":
    unittest.main()
