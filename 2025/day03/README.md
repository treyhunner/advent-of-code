# Day 03: Lobby

[Link to puzzle](https://adventofcode.com/2025/day/3)

The `len(bank)-count+i+1` bit took me a minute or two to get just right. I had an off-by-one error for a while and an off-by-many error before that.

I wish the string `index` method accepted keyword arguments so I could call `bank.index(battery, start=position)` instead of `bank.index(battery, position)`.
