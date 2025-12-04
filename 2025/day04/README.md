# Day 04: Printing Department

[Link to puzzle](https://adventofcode.com/2025/day/4)

I'm not very interested in the "check the surrounding rows and columns" challenges.
I rarely encounter this kind of thinking in my own work.

I enjoyed me use of the walrus operator in part 2.

I initially thought that my solution for part 2 was far too slow because my code was hanging.
It turns out I was just stuck in an accidentally infinite loop.


## On Performance

Some folks in the Python Discord noted that in previous Advent of Code years many folks would solve this kind of problem by making a set of complex numbers or a set of 2-item tuples to represent their grids.

I decided to try making a dictionary of 2-item tuples and then a dictionary of complex numbers to see how that felt.

I was surprised to see that this was noticeably slower.

```bash
$ python -m timeit 'from part2 import solve, parse_input; solve(parse_input("input.txt"))'
5 loops, best of 5: 94.8 msec per loop
$ python -m timeit 'from part2_dict_grid import solve, parse_input; solve(parse_input("input.txt"))'
1 loop, best of 5: 315 msec per loop
$ python -m timeit 'from part2_complex_grid import solve, parse_input; solve(parse_input("input.txt"))'
2 loops, best of 5: 183 msec per loop
```

I suspect the creation of 2-item tuples repeatedly for the dictionary lookups may have slowed this down.
The lookup within a dictionary may also be noticeably slower than the index checks in the list.
