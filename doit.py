#!/bin/env python

from __future__ import print_function

import datetime
import sys

MIN = 1
MAX = 10
BASE_PWR = 10
H = "0" * ( 10 ** BASE_PWR )


def eprint( *a, **k ):
    ''' Print to stderr
    '''
    print( *a, file=sys.stderr, **k )


def oneH():
    ''' Print one "H", which was originally a string of one-hundred zeros,
        but is now a string of zeros, the length of which is defined above.
    '''
    print(H)


def do_power_10_times( x, func ):
    ''' Do func "alotof" times, where "alotof" is defined as 10 to the "x" power
        PARAMS:
            x : integer : repeat "func" 10^x power times
            func : method reference : the function to called multiple times
    '''
    # Base case
    if x == 1:
        for i in range( 10 ):
            func()
    elif x > 1:
        for i in range( 10 ):
            do_power_10_times( x - 1, func )
    else:
        raise UserWarning( "exponent must be integer > 0" )


def run():
    eprint()
    eprint( "=" * 43 )
    eprint( "Time to print 10^{} * 10^n-th power of zeros".format( BASE_PWR ) )
    eprint( "-" * 43 )
    eprint( "Exponent, Total Zeros, Elapsed Seconds" )
    fmt = "{:>8}, {:>11}, {:>15f}"

    # Loop over increaseing powers of 10 till a pattern emerges in the output
    for power in range( MIN, MAX + 1 ):
        start_time = datetime.datetime.now()
        do_power_10_times( power, oneH )
        end_time = datetime.datetime.now()
        elapsed = end_time - start_time
        total_zeros = "10^" + str( ( power + BASE_PWR ) )
        eprint( fmt.format( power, total_zeros, elapsed.total_seconds() ) )

    eprint()
    eprint( "DONE" )
    eprint()

if __name__== "__main__":
    run()
