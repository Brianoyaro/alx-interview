#!/usr/bin/python3
'''module that rotates a 2D matrix in clockwise direction
'''


def rotate_2d_matrix(matrix):
    '''function implementing matrix rotation
    [Bug] This method fails when matrix is not an N*N matrix
    '''
    # print('debugging MATRIX before ANYTHING is {}'.format(matrix))
    # first transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    # print('debugging MATRIX before row reversal is {}'.format(matrix))

    # reverse each row
    for i in range(n):
        start = 0
        end = n - 1
        for j in range(int(n / 2)):
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            # print('wile  reversing, matrix is {}..........'.format(matrix))
            start += 1
            end -= 1
    # print('debugging MATRIX after row reversal is {}'.format(matrix))
