'''
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import numpy as np
from math import isqrt

MAX = 1000000 #test

def primes(a: int):

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

    arr = np.insert(arr, 2, [2, 3, 5, 7])
    arr = arr[arr!= 0]
    arr = arr[arr!= 1]

    return arr

def sum_primes(a: int):
    
    prime_arr = primes(a)
    half_len = round(len(prime_arr)/2)

    sol_sum = []
    sol_count = []
    
    #First we will test second half of the prime array. Given the numbers will be very large, only 2 members can be below 1M
    i = half_len
    while True:
        if prime_arr[i] + prime_arr[i+1] > MAX:
            break
        else:
            if prime_arr[i] + prime_arr[i+1] in prime_arr:
                sol_sum.append(prime_arr[i] + prime_arr[i+1])
                sol_count.append(2)
        i += 1
    
    #Now we will test first half of the array
    i = 0
    while i < half_len:
        j = i + 1
        s = prime_arr[i]
        count = 1
        while True:
            s = s + prime_arr[j]
            if s in prime_arr:
                sol_sum.append(s)
                sol_count.append(count+1)
            if s > MAX:
                break
            else:
                j += 1
                count += 1 

        i += 1
        
    #We have to choose the max count sum
    max_factors = max(sol_count)
    sum_ret = sol_sum[sol_count.index(max_factors)]

    return sum_ret, max_factors



def main():
    a = MAX
    print('Prime below 1M as consec sum and number count: ', sum_primes(a))

if __name__=='__main__':
    main()