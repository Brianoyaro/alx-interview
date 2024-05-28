#!/usr/bin/python3
'''N-Queens solution module
'''
import sys
if len(sys.argv) < 2:
    print('Usage: nqueens N')
    exit(1)
n = sys.argv[1]
for val in n:
    if ord(val) not in range(48, 58):
        print('N must be a number')
        exit(1)
n = int(n)
if n < 4:
    print('N must be at least 4')
    exit(1)


def solution(n):
    '''finds the solution of N-queens using backtracking
    '''
    col = set()
    posDiag = set()  # (r - c)
    negDiag = set()  # (r + c)
    board = [['.'] * n for _ in range(n)]
    result = []

    def backtrack(row):
        '''implements backtracking
        '''
        if row == n:
            copy = [''.join(row) for row in board]
            result.append(copy)
            return
        for column in range(n):
            if column in col or\
                    (row - column) in posDiag or\
                    (row + column) in negDiag:
                continue
            col.add(column)
            posDiag.add(row - column)
            negDiag.add(row + column)
            board[row][column] = 'Q'

            backtrack(row + 1)

            col.remove(column)
            posDiag.remove(row - column)
            negDiag.remove(row + column)
            board[row][column] = '.'
    backtrack(0)
    return result


results = solution(n)
for result in results:
    val = []
    for row_id, row in enumerate(result):
        col = row.index('Q')
        val.append([row_id, col])
    print(val)
