# googolplex
6th grade math extra credit

# Printing on paper is impossible
From wikipedia: [https://en.wikipedia.org/wiki/Googolplex]
> A typical book can be printed with 10<sup>6</sup> zeros (around 400 pages with 50 lines per page and 50 zeros per line). Therefore, it requires 10<sup>94</sup> such books to print all the zeros of a googolplex (that is, printing a googol of zeros). If each book had a mass of 100 grams, all of them would have a total mass of 10<sup>93</sup> kilograms. In comparison, Earth's mass is 5.972 x 10<sup>24</sup> kilograms, and the mass of the Milky Way Galaxy is estimated at 2.5 x 10<sup>42</sup> kilograms.

# What about printing on-screen?
This also takes a long time since screen updates are slow (compared to disk I/O). Disk I/O is slow compared to memory I/O.

# What about just printing to "nowhere"?
Printing to `/dev/null` should be the fastest "print" possible.  The program is still "print"-ing the data, but we are not looking at it.  It appears that even when printing to `/dev/null` a file system "open" call still happens, so printing a reasonably large string each time makes the most sense.

Consider the following example:
> Printing 10<sup>10</sup> zeros in groups of 100 took 99 seconds.
> 
> However, printing the same number of zeros in groups of 10000 took only 4 seconds.

I predict that printing 10<sup>100</sup>) zeros in ever larger groups will have similar results (ie: print more in less time). Finding the limit of these gains (by printing ever larger groups of zeros) is beyond the scope of this project.

To accomplish this (writing zeros to `/dev/null`), run the program as follows:
* `python doit.py > /dev/null`

# Patterns Evolve

