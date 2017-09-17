#!/usr/local/bin/python

import datetime
import sys
#import logging

MIN = 3
MAX = 6
BASE_PWR = 6
H = "0" * ( 10 ** BASE_PWR )
#VAL = 0


#def increment():
#    global VAL
#    VAL += 1
#    logging.debug( VAL )


def eprint( *a, **k ):
    print( *a, file=sys.stderr, **k )


def oneH():
    print(H)


def do_power_10_times( x, func ):
    # Base case
    if x == 1:
#        logging.debug( "base case" )
        for i in range( 10 ):
            func()
    elif x > 1:
#        logging.debug( "exponent={}".format( x ) )
        for i in range( 10 ):
            do_power_10_times( x - 1, func )
    else:
        raise UserWarning( "exponent must be integer > 0" )


def run():
    eprint()
    eprint( "=" * 43 )
    eprint( "Time to print 10^{} * 10^n-th power of zeros".format( BASE_PWR ) )
    eprint( "-" * 43 )
    eprint( "Exponent, Total Zeros, Elapsed Seconds, Micro-Seconds" )
    fmt = "{:>8}, {:>11}, {:>15}, {:>13}"

    for power in range( MIN, MAX + 1 ):
#        global VAL
#        VAL = 0
        start_time = datetime.datetime.now()
#        do_power_10_times( power, increment )
        do_power_10_times( power, oneH )
        end_time = datetime.datetime.now()
        elapsed = end_time - start_time
        total_zeros = "10^" + str( ( power + BASE_PWR ) )
        ( secs, microsecs ) = str( elapsed.total_seconds() ).split( '.' )
        eprint( fmt.format( power, total_zeros, secs, microsecs ) )
    eprint()
    eprint( "DONE" )
    eprint()

if __name__== "__main__":
#    logging.basicConfig( 
#        format='(%(funcName)s [%(lineno)s]):%(message)s', 
#        level=logging.WARNING
#        )
    run()

