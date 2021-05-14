'''
Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, 
it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
'''
from math import sqrt


def find_blues():
    '''
    import data to know: 
    1 - B/T and (B-1)/(T-1) must be close to equal at large numbers of B and T
    2 - B/T must be  B/T ~= sqrt(1/2)
    both end must be close to sqrt(1/2) due to 1
    sqrt(1/2)*T - 1 element < B < sqrt(1/2)*T + 1 element
    initial code took forever cause i was checking every single element until finding solution to 100, 1000, 10000, 100000, 10**6...
    while trying to create an efficient solution I found out (by luck not knowing what to do lol) each new solution begins exactly after multiplying the ratio of the 2 prvious values
    that value converges each time 5.828....
    i dont know what value is that, but its definitely important here
    with that, the solution is lighting fast! cool
    '''
    MAX = 10**12
    t = 10 + 1
    prev_b = []
    while True:
        b = round(sqrt(1/2)*t)
        i = b
        found = False
        while i < b+1:
            res = ((i/t)*((i-1)/(t-1)))*2
            #print(res)
            if round(res, 15) == 1: #Python not calculating properly...
                prev_b.append(i)
                found = True
                if t > 10**12:
                    return i, prev_b
            i += 1
        #print(t)
        if len(prev_b) >= 2 and found==True:
            t = round(t*prev_b[len(prev_b)-1]/prev_b[len(prev_b)-2])
        else:
            t += 1

def main():
    
    print('number of blue discs: ', find_blues())

if __name__=='__main__':
    main()
