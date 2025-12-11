# Day 10: Factory

[Link to puzzle](https://adventofcode.com/2025/day/10)

Part 1 involved bit-wise stuff that I don't think about often.
It was okay.

Part 2 I could not manage to make even semi-reasonably efficient...
until I realized that libraries for solving linear equations were probably a thing.

Chat GPT turned my linear equation solving idea into working code that uses the [pulp][] library.
I refactored the code and made sure I understood the parts.

The next time I have a problem that can be modeled as a series of linear equations, I'll reach for this library.

My code for part 2 takes 1 second to run!

```bash
$ time ./part2.py > /dev/null
./part2.py > /dev/null  0.62s user 0.35s system 100% cpu 0.966 total
```


[pulp]: https://coin-or.github.io/pulp/
