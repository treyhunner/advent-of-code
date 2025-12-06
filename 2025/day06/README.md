# Day 06: Compactor

[Link to puzzle](https://adventofcode.com/2025/day/6)

Yuck.

Similar to a couple Python Morsels exercises, but more frustrating.

I enjoyed having excuses to:
- Remember that `zip(*...)` transposes
- Use extended tuple unpacking with a list-like syntax (`[*numbers, operators] = ...`)
- Recall `math.prod` which I rarely use

My [initial][1] part 2 was pretty nasty looking.
I eventually [refactored][2] it to use `itertools.groupby` and to embrace comprehensions more heavily.
It's pretty dense now, but I actually think it's a bit more readable now.

I then decided to [refactor again][3] to split by blank lines by using a regular expression instead of using `groupby`.


[1]: https://github.com/treyhunner/advent-of-code/blob/33f255ba7547f23595faa7f7836c2c3f52c811ac/2025/day06/part2.py
[2]: https://github.com/treyhunner/advent-of-code/blob/b4a8cd8754c199fb038780713635fd9966bbc422/2025/day06/part2.py
[3]: https://github.com/treyhunner/advent-of-code/blob/5042b485e7987acf3c654d4b7ee6ec98dd725fe9/2025/day06/part2.py
