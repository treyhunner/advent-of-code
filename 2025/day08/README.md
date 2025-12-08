# Day 08: Playground

[Link to puzzle](https://adventofcode.com/2025/day/8)

The code is long and ugly for both parts but the mostly brute force approach worked without an issue.

This was the first day I felt that a class would really come in handy.
I am somewhat proud of my frozen, orderable, hashable, subtractable dataclass that used match-case for a good purpose and has a magnitude property.
All the features served a purpose.

Interestingly, I seemed to use more fun tricks in part 1 than part 2.
Both used `deque` and involved lexicographical sorting, but part 1 also used `frozenset`, `heapq.nlargest` and `math.prod`.

Part 2 *did* end up using a set of object IDs, which is a hack that I'm pretty sure could have been done differently (weak references maybe or just frozen sets or something) but I didn't think up an alternative quickly.

## Update

After sleeping on the problem and taking a look at my code again, I made some additional refactorings:

- Used `itertools.combinations`: this avoided a nested loop, the need to make a dictionary of sorted point pairs (to avoid storing both `(p, q)` and `(q, p)`), and the need for an identity or equality check to skip over `(p, p)` pairings of the point with itself
- Swapped the `if` condition in the last loops since the `if` was simply `continue`
- Used `dict.fromkeys` (I can't believe I overlooked this one as I teach `fromkeys` often)
- Initially refactored part 2 to use a list of weak references to circuit sets
- Refactored part 2 again to just use a list of the circuit sets and then called `remove` to remove circuit sets (this was way more readable than the "is the reference count 0" logic I had in the in-between refactoring)

- Before: [part 1][1] and [part 2][2]
- Weak reference refactoring: [part 2][3]
- After: [part 1][4] and [part 2][5]

[1]: https://github.com/treyhunner/advent-of-code/blob/807ff2039b887b9c7d80d05d59067c91de404459/2025/day08/part1.py
[2]: https://github.com/treyhunner/advent-of-code/blob/807ff2039b887b9c7d80d05d59067c91de404459/2025/day08/part2.py
[3]: https://github.com/treyhunner/advent-of-code/blob/b820a476b4bd3b155f044f4a2a20bf6eeceee023/2025/day08/part2.py
[4]: https://github.com/treyhunner/advent-of-code/blob/b79fdb79b3572cf3553faab79201181348ef19ca/2025/day08/part1.py
[5]: https://github.com/treyhunner/advent-of-code/blob/b79fdb79b3572cf3553faab79201181348ef19ca/2025/day08/part2.py
