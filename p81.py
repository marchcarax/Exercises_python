'''
Problem 81
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt 
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
'''

def find_min_path(matrix_list: list):
    best_sum = []
    best_sum.append(matrix_list[0][0])
    n=len(matrix_list)
    sol = [[0 for i in range(n)] for j in range(n)]
    sol[0][0] = matrix_list[0][0]
    for i in range(1, n):
        sol[i][0] = matrix_list[i][0] + sol[i - 1][0]
        for j in range(1, n):
            sol[0][j] = matrix_list[0][j] + sol[0][j - 1]
            sol[i][j] = matrix_list[i][j] + min(sol[i-1][j], sol[i][j-1])
    
    return sol[-1][-1], len(sol)

def main():
    matrix_list = []

    with open ("p081_matrix.txt") as myfile:
        data = myfile.readlines()
        
    for line in data:
        split_line = line.strip().split(",") 
        nums_ls = [int(x) for x in split_line] # get rid of the quotation marks and convert to int
        matrix_list.append(nums_ls)

    print('min_path: ', find_min_path(matrix_list))

if __name__=='__main__':
    main()