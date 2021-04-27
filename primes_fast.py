'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

MUCH faster version. Not mine
'''

import numpy as np
from math import isqrt
from bitarray import bitarray

def sum_of_primes_below(n):
    primes_in_range = bitarray(n)
    primes_in_range.setall(False)

    primes_in_range[2] = True      # 2 is a prime
    primes_in_range[3::2] = True   # Odd numbers starting at 3 are prime candidates

    for d in range(3, isqrt(n) + 1, 2):
        if primes_in_range[d]:
            primes_in_range[d*d::2*d] = False    # Reset multiples of prime candidate
    
    return sum(idx for idx, flag in enumerate(primes_in_range) if flag)

def main():
    a = 2000000
    print('number of primes less than a: ', sum_of_primes_below(a))

if __name__=='__main__':
    main()