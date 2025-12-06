# Day 06: Compactor

[Link to puzzle](https://adventofcode.com/2025/day/6)

Yuck.

Similar to a couple Python Morsels exercises, but more frustrating.

I enjoyed having excuses to:
- Remember that `zip(*...)` transposes
- Use extended tuple unpacking with a list-like syntax (`[*numbers, operators] = ...`)
- Recall `math.prod` which I rarely use

My initial part 2 was pretty nasty looking.
I eventually refactored it to use `itertools.groupby` and to embrace comprehensions more heavily.
It's pretty dense now, but I actually think it's a bit more readable now.
