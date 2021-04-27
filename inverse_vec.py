'''
 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before
'''

import  numpy as np

def inverse_arr(arr):
    arr = np.array(arr)

    i=0
    inv = []
    while i < len(arr):
        inv.append(arr[len(arr)-i-1])
        i += 1
    return inv

def main():
    a = [2,3,5,1,2,4,7,9,3,6,13,4, 5666666, 2,313, 0]
    print('a: ', a)
    print('inverse of a: ', inverse_arr(a))

if __name__=='__main__':
    main()