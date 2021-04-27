#Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.

import numpy as np

def minmax(arr):
    arr = np.sort(arr)
    arr = np.array([arr[0], arr[len(arr)-1]])
    return arr

def main():
    list_a = [2,3,5,1,2,4,7,9,3,6,13,4, 5666666, 2,313, 0]
    arr = np.array(list_a)
    print('minmax of arr: ', minmax(arr))

if __name__=='__main__':
    main()
