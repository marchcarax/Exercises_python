'''
Advent of code 2020 
Day 2: Password Philosophy
Find the correct passwords
'''

import numpy as np


def correct_pswd(pwd_list):

    total=len(pwd_list)
    correct=0
    for i in range(0, total):
        min_times = int(pwd_list[i][:pwd_list[i].find('-')])
        max_times = int(pwd_list[i][pwd_list[i].find('-')+1:pwd_list[i].find(' ')])
        letter = pwd_list[i][pwd_list[i].find(' ')+1:pwd_list[i].find(':')]
        pwd = pwd_list[i][pwd_list[i].find(':')+2:]
        #print(pwd)
        if min_times <= pwd.count(letter) <= max_times:
            correct += 1

    return correct

def correct_pswd_v2(pwd_list):

    total=len(pwd_list)
    correct=0
    for i in range(0, total):
        min_times = int(pwd_list[i][:pwd_list[i].find('-')])
        max_times = int(pwd_list[i][pwd_list[i].find('-')+1:pwd_list[i].find(' ')])
        letter = pwd_list[i][pwd_list[i].find(' ')+1:pwd_list[i].find(':')]
        pwd = pwd_list[i][pwd_list[i].find(':')+2:]
        #print(pwd)
        if (pwd[min_times-1] == letter) ^ (pwd[max_times-1] == letter):
            correct += 1

    return correct

def main():
    
    try:
        pwd_list = []
        while True:
            pwd_list.append(input())
    except:
        print('List read')

    print('correct passwords version 1: ', correct_pswd(pwd_list))
    print('correct passwords version 2: ', correct_pswd_v2(pwd_list))

if __name__=='__main__':
    main()