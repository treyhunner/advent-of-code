# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python.

## Structure

Each day's solution follows this structure:
- `part1.py` - Solution for part 1
- `part2.py` - Solution for part 2
- `test_dayXX.py` - Tests using sample inputs
- `sample.txt` - Example input from the puzzle
- `input.txt` - Personal puzzle input
- `README.md` - Notes

## Running Solutions

Run a specific day's solution:

```bash
cd 2025/day01
python part1.py
python part2.py
```

Run tests:

```bash
python -m unittest test_day01.py
# Or run all tests in a directory
python -m unittest discover -s 2025/day01
```

## Creating New Days

Use the automation script to scaffold a new day:

```bash
python scripts/new_day.py 2
```

This creates the directory structure and template files for day 2.
