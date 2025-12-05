# Day 05: Cafeteria

[Link to puzzle](https://adventofcode.com/2025/day/5)

I initially intersected 2 sets for part 1, like this:

```python
return len(available_ids & parse_ranges(fresh_ranges))
```

Running that on the sample worked fine but running on the full input froze my machine for a minute until Python crashed.

Don't try to make a set of trillions of numbers.


## More range parsing

This was pretty much a continuation of day 02.

I benefited from my recollection of the sorting that I did for some of the `parse_range` Python Morsels exercise solutions.
I did have to think for a bit about overlapping versus non-overlapping ranges, but part 2 ended up coming pretty naturally after the sorting.
