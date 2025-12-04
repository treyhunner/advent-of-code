"""Day 04 - Part 2"""
from pathlib import Path


def parse_input(filename):
    grid = (Path(__file__).parent / filename).read_text().splitlines()
    return {
        (x, y): value
        for x, row in enumerate(grid)
        for y, value in enumerate(row)
    }


def adjacent(grid, x, y):
    """Return the (up to 8) cells adjacent to (x, y)."""
    return [
        grid[x+n, y+m]
        for n in range(-1, 2)
        for m in range(-1, 2)
        if not (n == m == 0) and (x+n, y+m) in grid
    ]


def remove_rolls(grid):
    """Remove all rolls (@) with fewer than 4 rolls adjacent to them."""
    accessible = 0
    for (x, y), item in grid.items():
        if item == "@" and adjacent(grid, x, y).count("@") < 4:
            grid[x, y] = "x"
            accessible += 1
    return accessible


def solve(grid):
    """Repeadetly remove all removable rolls from the grid."""
    accessible = 0
    while removed := remove_rolls(grid):
        accessible += removed
    return accessible


if __name__ == "__main__":
    print(f"Sample: {solve(parse_input('sample.txt'))}")
    print(f"Solution: {solve(parse_input('input.txt'))}")
