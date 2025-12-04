"""Tests for Day 04"""
import unittest
import part1
import part2
import part2_dict_grid


class TestDay04(unittest.TestCase):
    """Test Advent of Code Day 4 solutions"""

    def test_part1_sample(self):
        data = part1.parse_input("sample.txt")
        result = part1.solve(data)
        self.assertEqual(result, 13)

    def test_part2_sample(self):
        data = part2.parse_input("sample.txt")
        result = part2.solve(data)
        self.assertEqual(result, 43)

    def test_part2_with_dictionary_grid(self):
        data = part2_dict_grid.parse_input("sample.txt")
        result = part2_dict_grid.solve(data)
        self.assertEqual(result, 43)


if __name__ == "__main__":
    unittest.main()
