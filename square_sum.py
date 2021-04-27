'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

import numpy as np

def squaresum(a: int):
    arr = np.arange(a) * np.arange(a)
    arr = np.sum(arr)
    return arr


'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''

def squaresumodds(a: int):
    arr = np.arange(a) * np.arange(a)
    i = 0
    res = []
    while i < len(arr):
        if bool(arr[i]&(1<<0)):
            res.append(1)
        else:
            res.append(0)
        i += 1
    arr = arr * np.array(res)
    arr = np.sum(arr)
    return arr

'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
def sumsquaredif(a: int):
    sum_squares = squaresum(a)
    arr = np.arange(a)
    arr = np.sum(arr)*np.sum(arr)
    return (arr - sum_squares)


def main():
    a = 101
    print('a vector: ', np.arange(a))
    print('sum of squares of a: ', squaresum(a))
    print('sum of squares of odds of a: ', squaresumodds(a))
    print('difference between sum of squares: ', sumsquaredif(a))

if __name__=='__main__':
    main()