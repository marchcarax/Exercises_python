#Create a function that returns if a is multiple of b:

def is_multiple(a: int, b: int):

    if b%a == 0:
        return True
    else:
        return False

def is_odd(a:int):
    #bit = bin(a)
    #look into last bit (0) if its a 1 or 0
    return bool(a&(1<<0))

def main():
    print('a multiple of b: ', is_multiple(5,12))
    print('a is even: ', is_multiple(2, 6))
    print('a is odd: ', is_odd(100023124348))

if __name__=='__main__':
    main()
