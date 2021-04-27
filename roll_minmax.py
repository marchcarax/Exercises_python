#create a rolling max and rollling min function given an array and window lenght input
#output for each function must be an array with same lenght with the max/min integer at each window lenght
#MUST: use numpy for speed 



import numpy as np


def strided_app(a, L, S ):  # Window len = L, Stride len/stepsize = S
    nrows = ((a.size-L)//S)+1
    n = a.strides[0]
    return np.lib.stride_tricks.as_strided(a, shape=(nrows,L), strides=(S*n,n))

#Computes max given a window W and an array a
def max_filter1d_valid_strided(a, W):
    return strided_app(a, W, S=1).max(axis=1)

#Computes min given a window W and an array a
def min_filter1d_valid_strided(a, W):
    return strided_app(a, W, S=1).min(axis=1)

#Computes mean given a window W and an array a
def mean_filter1d_valid_strided(a, W):
    return strided_app(a, W, S=1).mean(axis=1)

def main():

    window = 3
    arr = np.array([1, 2, 30, 4, 5, 1, 5, 1, 5, 2, 0])
    
    max_arr = max_filter1d_valid_strided(arr, window)
    max_arr = np.insert(max_arr, 0, np.zeros(window-1))
    print(max_arr)

    min_arr = min_filter1d_valid_strided(arr, window)
    min_arr = np.insert(min_arr, 0, np.zeros(window-1))
    print(min_arr)

    mean_arr = mean_filter1d_valid_strided(arr, window)
    mean_arr = np.insert(mean_arr, 0, np.zeros(window-1))
    print(mean_arr)


if __name__ == "__main__":
    main()