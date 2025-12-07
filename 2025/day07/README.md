# Day 07: Laboratories

[Link to puzzle](https://adventofcode.com/2025/day/7)

I cheated for part 2 by looking up how to calculate the possibilities.

Once I realized adding up the number of splitters that could have gone down a beam path was the trick (for the double splitter merged beams that is), it was clear that `collections.Counter` was the way to go.

I enjoyed using the new(ish) `total` method on `Counter`.

After I solved it I saw mention of recursion and caching and realized that my recursive solution which was far too slow (due to all the Fibonacci-style absurd forking) could be fixed with `functools.cache`.

- Part 2: [before - with `Counter`][1]
- Part 2: [after - with recursion and caching][2]

[1]: https://github.com/treyhunner/advent-of-code/blob/37e5978bd1073a070114086ce29f0e3d459043fc/2025/day07/part2.py
[2]: https://github.com/treyhunner/advent-of-code/blob/c57f732ecbe93ad051795bc0b73f7af4fe137c6e/2025/day07/part2.py
