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


def main():
    a = 12
    print('sum of squares of a: ', squaresum(a))
    print('sum of squares of odds of a: ', squaresumodds(a))

if __name__=='__main__':
    main()