'''
Advent of code 2020 
Day 1: Report Repair
Find the two entries that sum to 2020; what do you get if you multiply them together?
'''

import numpy as np


def find_num(num_list):

    total=2020
    i=0
    while i < len(num_list):
        num = total - num_list[i]
        j = i + 1
        while j < len(num_list):
            if num == num_list[j]:
                return num_list[j]*num_list[i]
            else:
                j += 1
        i += 1
    return None

def find_threes(num_list):

    total=2020
    i=0
    while i < len(num_list):
        j = i + 1
        while j < len(num_list):
            if total > num_list[i] + num_list[j]:
                k = j + 1
                num = total - num_list[i] - num_list[j]
                while k < len(num_list):
                    if num_list[k] == num:
                        return num_list[i]*num_list[j]*num_list[k]
                    else:
                        k += 1
            j += 1
        i += 1
    return None

def main():
    
    try:
        num_list = []
        
        while True:
            num_list.append(int(input()))
    except:
        print('List read')
    # if the input is not-integer, just print the list

    print('number is: ', find_num(num_list))
    print('3 numbers mul:', find_threes(num_list))

if __name__=='__main__':
    main()