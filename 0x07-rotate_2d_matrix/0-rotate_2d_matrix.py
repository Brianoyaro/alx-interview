#!/usr/bin/python3
'''module that rotates a 2D matrix in clockwise direction
'''


def rotate_2d_matrix(matrix):
    '''function implementing matrix rotation
    [
        [1,2,3],
        [4,5,6],
        [7,8,9] ]
    '''
    # first transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse each row
    for i in range(n):
        for j in range(int(n / 2)):
            start = 0
            end = n - 1
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            start += 1
            end -= 1
