# Day 08: Playground

[Link to puzzle](https://adventofcode.com/2025/day/8)

The code is long and ugly for both parts but the mostly brute force approach worked without an issue.

This was the first day I felt that a class would really come in handy.
I am somewhat proud of my frozen, orderable, hashable, subtractable dataclass that used match-case for a good purpose and has a magnitude property.
All the features served a purpose.

Interestingly, I seemed to use more fun tricks in part 1 than part 2.
Both used `deque` and involved lexicographical sorting, but part 1 also used `frozenset`, `heapq.nlargest` and `math.prod`.

Part 2 *did* end up using a set of object IDs, which is a hack that I'm pretty sure could have been done differently (weak references maybe or just frozen sets or something) but I didn't think up an alternative quickly.
