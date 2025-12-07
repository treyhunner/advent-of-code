# Day 07: Laboratories

[Link to puzzle](https://adventofcode.com/2025/day/7)

I cheated for part 2 by looking up how to calculate the possibilities.

Once I realized adding up the number of splitters that could have gone down a beam path was the trick (for the double splitter merged beams that is), it was clear that `collections.Counter` was the way to go.

I enjoyed using the new(ish) `total` method on `Counter`.
