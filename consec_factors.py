'''
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

ITS SUPER SLOW LOL, but works
'''


import numpy as np
from math import sqrt
from functools import reduce

#great function found in stackoverflow by agf
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def distinct_factors(l: set):

    arr = np.array(list(l)).astype(np.int32)

    for i in range(1, len(arr)):
        if np.isin(sqrt(arr[i]), arr):
            arr[i] = 0
        if arr[i] != 0:
            if len(list(factors(arr[i]))) > 3:
                arr[i] = 0

    a = arr[arr != 0]
    return a


def find_distinct_factors():
    i = 600 #we already know it has to be higher than 644
    number_factors = 4
    while True:
        j = 1
        fact = distinct_factors(factors(i))
        if (len(fact) - 1) == number_factors:
            fact_fut = distinct_factors(factors(i+1))
            if (len(fact_fut) - 1) == number_factors:
                fact_fut2 = distinct_factors(factors(i+2))
                if (len(fact_fut2) - 1) == number_factors:
                    fact_fut3 = distinct_factors(factors(i+3))
                    if (len(fact_fut3) - 1) == number_factors:
                        return i, i+1, i+2, i+3
                    else:
                        j = 4 #if future i+3 fails, begin calcs in i+4
                else:
                    j = 3 #if future i+2 fails, begin calcs in i+3
            else:
                j = 2 #if future i+1 fails, begin calcs in i+2

        if i == 10000000:
            return i

        i += j

def main():
    
    print('factors of a: ', find_distinct_factors())
    #print(distinct_factors(factors(644),644))

if __name__=='__main__':
    main()