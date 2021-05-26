'''
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them 
in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''


import numpy as np
from math import isqrt, sqrt
from functools import reduce


def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def isprime(a: int):
    if len(list(factors(a))) > 2:    
        return False
    else:
        return True

def concat_str(a: int, b: int):
    if isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a))):
        return True
    else:
        return False

def primearr(a: int):

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
    arr = arr[arr != 0]
    arr = arr[arr != 1]
    print('array generated')

    return arr

def concat_primes(num: int, max_len: int, max_prime: int):

    arr = primearr(max_prime)

    if num > 1:
        i = 1 #can't be 2, so it begins in 3
        while int(arr[i]) < 100: #let's try first batch of small i, so computation dont go crazy
            res = []
            j = i + 1
            while len(str(int(arr[j]))) < max_len:
                if (concat_str(int(arr[i]), int(arr[j]))):
                    if num > 2:            
                        k = j + 1
                        while len(str(int(arr[k]))) < max_len:
                            if (concat_str(int(arr[i]), int(arr[k])) and
                                concat_str(int(arr[j]), int(arr[k]))):
                                if num > 3:        
                                    l = k + 1
                                    while len(str(int(arr[l]))) < max_len:
                                        if (concat_str(int(arr[i]), int(arr[l])) and
                                            concat_str(int(arr[j]), int(arr[l])) and
                                            concat_str(int(arr[k]), int(arr[l]))):
                                            #print(res)
                                            if num > 4:  
                                                m = l + 1
                                                while len(str(int(arr[m]))) < max_len:
                                                    if (concat_str(int(arr[i]), int(arr[m])) and
                                                        concat_str(int(arr[j]), int(arr[m])) and
                                                        concat_str(int(arr[k]), int(arr[m])) and
                                                        concat_str(int(arr[l]), int(arr[m]))):
                                                        res.append(int(arr[i]))
                                                        res.append(int(arr[j]))
                                                        res.append(int(arr[k]))
                                                        res.append(int(arr[l]))
                                                        res.append(int(arr[m]))
                                                        return np.array(res).sum(), res
                                                    m += 1
                                            else:
                                                res.append(int(arr[i]))
                                                res.append(int(arr[j]))
                                                res.append(int(arr[k]))
                                                res.append(int(arr[l]))
                                                return np.array(res).sum(), res
                                        l += 1
                                else:
                                    res.append(int(arr[i]))
                                    res.append(int(arr[j]))
                                    res.append(int(arr[k]))
                                    return np.array(res).sum(), res
                            k += 1
                    else:
                        res.append(int(arr[i]))
                        res.append(int(arr[j]))
                        return np.array(res).sum(), res
                j += 1
            i += 1
                                        
    return None


def main():
    num = 5 #to test if with 4 numbers it works, then try with 5
    max_str_len = 5 #keep increasing until finding a solution
    max_prime = 1000000
    print('sum of prime pairs: ', concat_primes(num, max_str_len, max_prime))

if __name__=='__main__':
    main()