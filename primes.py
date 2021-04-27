'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import numpy as np
from math import isqrt

def primesum(a: int):

    arr = np.arange(a, dtype = int)
    zero = np.zeros(a)

    arr = np.where(arr%2 == 0, zero, arr)
    arr = np.where(arr%3 == 0, zero, arr)
    arr = np.where(arr%5 == 0, zero, arr)
    arr = np.where(arr%7 == 0, zero, arr)

    i = 7
    while i < (isqrt(len(arr))+1):
        if arr[i] != 0:
            if arr[i]%i == 0:
                arr = np.where(arr%i == 0, zero, arr)
                arr[i] = i
        i += 1

    arr = np.insert(arr, 0, [2, 3, 5, 7])
    arr = arr.sum() - 1 

    return arr

def main():
    a = 2000000
    print('number of primes less than a: ', primesum(a))

if __name__=='__main__':
    main()