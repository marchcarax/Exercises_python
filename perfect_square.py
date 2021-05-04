'''
Problem 142

Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.

Solution takes forever, but it finds the solution. Either Python is too slow or my code is baaad (most probable...)
'''

import numpy as np
from math import isqrt

def is_odd(a:int):
    return bool(a&(1<<0))

def perfect_square():
    '''
    
    What is sure is that:
    x + y = a*a --> x = A - y ; A is the max arr_square[i] value ; 
    x - y = b*b --> y = x - B ; x > B ; adding first 2 formulas: x = (A + B)/2 --> must be even --> both A and B must be either odd or even
    x + z = c*c --> x = C - z ; C is the second biggest; z = C - x --> c*c > x --> c > sqrt(x)
    x - z = d*d --> z = x - D ; x > B > D
    y + z = e*e --> y = E - z ; 
    y - z = f*f --> z = y - F; F is the smallest arr_square[i] value

    '''
    #First I create the list of perfect squares
    arr_square = np.arange(1000)*np.arange(1000)
    
    x = 3
    y =  2 
    z = 1 #must be min >0
    i = 1

    while True:
        for a in range(5, 1000000):
            if is_odd(a):
                minb = 1 #both A and B must be odd or even
            else:
                minb = 2 #both A and B must be odd or even
            for b in range(minb, a-2, 2):
                if a > b and (a*a + b*b)%2 == 0:
                    x = int((a*a + b*b)/2) 
                    y = int(x - b*b) 
                    if x > y > 0 and (x - y) in arr_square:
                        for c in range(isqrt(x)+1, a-1):
                            if y > (c*c - x):
                                z = int(c*c - x) 
                                #print(x, y, z)
                                if (y + z)  in arr_square:
                                    print('2on stage: ', x, y, z)
                                    if (y - z)  in arr_square:
                                        print('Pre-final stage: ', x, y, z)
                                        if (x - z)  in arr_square:
                                            return x, y, z, x+y+z

        i += 1
        if i == 100000:
            return None

def main():
    print('x+y+z is: ', perfect_square())

if __name__=='__main__':
    main()
