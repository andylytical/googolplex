# googolplex
6th grade math extra credit

# Printing on paper is impossible
From wikipedia: [https://en.wikipedia.org/wiki/Googolplex]
> A typical book can be printed with 10<sup>6</sup> zeros (around 400 pages with 50 lines per page and 50 zeros per line). Therefore, it requires 10<sup>94</sup> such books to print all the zeros of a googolplex (that is, printing a googol of zeros). If each book had a mass of 100 grams, all of them would have a total mass of 10<sup>93</sup> kilograms. In comparison, Earth's mass is 5.972 x 10<sup>24</sup> kilograms, and the mass of the Milky Way Galaxy is estimated at 2.5 x 10<sup>42</sup> kilograms.

# What about printing on-screen?
This also takes a long time since screen updates are slow (compared to disk I/O). Disk I/O is slow compared to memory I/O.

# What about just printing to "nowhere"?
### Reasoning
Printing to `/dev/null` should be the fastest "print" possible.  The program is still "print"-ing the data, but we are not looking at it.  It appears that even when printing to `/dev/null` a file system "open" call still happens, so printing a reasonably large string each time makes the most sense.

Consider the following example:
> Printing 10<sup>10</sup> zeros in groups of 100 took 99 seconds.
> 
> However, printing the same number of zeros in groups of 10000 took only 4 seconds.

It follows that printing 10<sup>100</sup> zeros in even larger groups would require even less time). Finding the limit of these gains (by printing ever larger groups of zeros) is beyond the scope of this project.

### Method
To run the program so that the output is written to `/dev/null`:
* `python doit.py > /dev/null`

# Verifying Correctness
To verify correct output, pipe stdout to the `wc` (word counter) program:
* `python doit.py | wc -l`

# Patterns Evolve
```
===========================================
Time to print 10^8 * 10^n-th power of zeros
-------------------------------------------
Exponent, Total Zeros, Elapsed Seconds
       3,       10^11,        0.002728
       4,       10^12,        0.023774
       5,       10^13,        0.238504
       6,       10^14,        2.393172
       7,       10^15,       23.795959
       8,       10^16,      237.735227
       9,       10^17,     2382.038372
      10,       10^18,    24068.190496
```
```
===========================================
Time to print 10^10 * 10^n-th power of zeros
-------------------------------------------
Exponent, Total Zeros, Elapsed Seconds
       1,       10^11,        0.000251
       2,       10^12,        0.000863
       3,       10^13,        0.007722
       4,       10^14,        0.076729
       5,       10^15,        0.767348
       6,       10^16,        7.663548
       7,       10^17,       77.189416
       8,       10^18,      767.758355
       9,       10^19,     7783.759926
      10,       10^20,    
```
The output shown is from two runs using different lengths for the string of zeros that was printed for each line.  The patterns discussed are identical in each run (as well as other runs that are not shown here).

### Run time is linearly proportional to output size
In all but the very first iteration, the following pattern emerges: as the output size increases one order of magnitude, the runtime (in seconds) also increases by one order of magnitude. All the runtime estimates that follow are based on this analysis of the pattern.

### Relationship between output size and runtime (in seconds)
When printing lines of length 10<sup>10</sup>, the runtime in seconds is 10<sup>-15</sup> * the output size.  For example, printing 10<sup>16</sup> zeros takes (on the order of): 10<sup>16</sup> * 10<sup>-15</sup> = 10<sup>1</sup>. In other words, the time to print 10<sup>16</sup> zeros requires between 1-9 seconds.  This pattern holds true for all oputput sizes tested (up to 10<sup>20</sup> zeros).  Further timing samples were not run since the expected runtime is on the order of days and weeks.

# Prediction
Using the model above, the time required to print 10<sup>100</sup> zeros is on the order of 10<sup>86</sup> seconds.  This is equivalent to 10<sup>82</sup> hours, which is equivalent to 10<sup>76</sup> centuries.

# Additional Thoughts
All the iterations performed above ran on a single core of an era 2015 computer.

## Could parallel computing improve the runtime?
Printing the zeros on 2 cores in parallel would cut the time in half. Likewise, using 10 cores would reduce the time by a factor of 10. Another way to state that is: running on 10 cores would result in a 10<sup>-1</sup> adjustment in total runtime.  Modern supercomputers have on the order of 10<sup>5</sup> cores ([Blue Waters](https://bluewaters.ncsa.illinois.edu/hardware-summary) has about 400,000 cores). Printing 10<sup>100</sup> zeros on the Blue Waters supercomputer would take approximately 10<sup>76</sup> * 10<sup>-5</sup> = 10<sup>71</sup> centuries.  That doesn't help very much.

# Conclusion
Googolplex is a really, *really*, **_really_**, **really** **BIG** number.  To quote Megamind, "It's unfathomable"!
