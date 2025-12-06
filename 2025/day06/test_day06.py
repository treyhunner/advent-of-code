"""Tests for Day 06"""
import unittest
import part1
import part2


class TestDay06(unittest.TestCase):
    """Test Advent of Code Day 6 solutions"""

    def test_part1_sample(self):
        data = part1.parse_input("sample.txt")
        result = part1.solve(data)
        self.assertEqual(result, 4277556)

    def test_part2_sample(self):
        data = part2.parse_input("sample.txt")
        result = part2.solve(data)
        self.assertEqual(result, 3263827)


if __name__ == "__main__":
    unittest.main()
