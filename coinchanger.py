import sys
from time import *
import timeit

COINS = [1, 2, 5, 10, 20, 50]

def coinChanger(change):
    # base case for recursion function to end
    if change == 0:
        return
    else:
        coin = COINS.pop()
        # divmod gives much better performance on big numbers than normal division
        # and mod
        counter, remainder = divmod(change, coin)
        # Does not print coins that have a counter of 0
        if counter > 0:
            print'{} * {} cent coins'.format(counter, coin)
        return coinChanger(remainder)


try:
    change = input('Enter your change in cents:\n')
    if (isinstance(change, int)) and (change >= 0) and (change < sys.maxint):
        coinChanger(change)
    else:
        print "Please enter a whole number within range"
except Exception as e:
    print 'Caught the exception: ', e
#causes a time delay so the executable doesn't close immediately
t1 = timeit.Timer()
print t1.timeit()
sleep(5)
