'''
Problem 90
In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
'''

import numpy as np
from itertools import permutations, combinations

def all_comb(k: int, n: int):
    sides = np.arange(n)
    cubes = combinations(sides, 6) #all possible cubes
    all_comb = [] #will change all permutations so it only includes 6 and not 6,9
    for i in cubes:
        j = 0
        side_arr = list(i)
        side_no_9 = []
        while j < len(side_arr):
            if side_arr[j] == 9:
                side_no_9.append(6)
            else:
                side_no_9.append(side_arr[j])
            j += 1
        all_comb.append(side_no_9)
    
    return all_comb

def list_contains(lista, n):
    lista = np.array(lista)
    if n in lista:
        return True
    else:
        return False

def is_square(list_1, list_2):
    square_arr = [[0, 1], [0,4], [0,6], [1,6], [2,5], [3,6], [4,6], [6,4], [8,1]]
    for i in square_arr:
        if not ((list_contains(list_1, i[0]) and list_contains(list_2, i[1]) or
            (list_contains(list_2, i[0]) and list_contains(list_1, i[1])))):
            return False
    return True

def sum_of_cube_pairs(k, n):
    combs = all_comb(k, n)
    i = 0
    res = 0
    while i < len(combs):
        if combs[i][0] != 0:
            break
        j = i
        while j < len(combs) - 1:
            j += 1
            if is_square(combs[i], combs[j]):
                res += 1
        i += 1
    return res


def main():
    max_arr = 10
    sides = 6
    print('total different arrangements: ', sum_of_cube_pairs(sides, max_arr))

if __name__=='__main__':
    main()