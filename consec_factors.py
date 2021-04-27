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


#want to erase the 1, n, and factors that are not distinct
def distinct_factors(l: list, i: int):
    res = []
    arr = np.array(list(l))
    zeros = np.zeros(len(arr))

    for i in range(1, len(arr)):
        if np.isin(sqrt(arr[i]), arr):
            arr[i] = 0
        if arr[i] != 0:
            if len(list(factors(arr[i]))) > 3:
                arr[i] = 0

    a = arr[arr != 0]
    return a

#for 2 works fine
def find_distinct_factors():
    i = 600 #we already know it has to be higher than 644
    number_factors = 4
    while True:
        fact = distinct_factors(factors(i), i) 
        fact_prev = distinct_factors(factors(i+1), i+1)
        fact_prev2 = distinct_factors(factors(i+2), i+2)
        fact_prev3 = distinct_factors(factors(i+3), i+3)
        
        if (len(fact) - 1) == number_factors and (len(fact_prev) - 1) == number_factors and (len(fact_prev2) - 1) == number_factors:
            if (len(fact_prev3) - 1) == number_factors:
                return i, i+1, i+2, i+3

        if i == 10000000:
            return i

        i += 1

def main():
    
    print('factors of a: ', find_distinct_factors())
    #print(distinct_factors(factors(644),644))

if __name__=='__main__':
    main()