#!/usr/bin/python3
'''island perimeter
'''


def island_perimeter(grid):
    '''finds the perimeter of an island
    '''
    columns = len(grid[0])
    rows = len(grid)
    answers = []
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                topRow = row - 1 if row - 1 >= 0 else 'Null'
                bottomRow = row + 1 if row + 1 <= rows else 'Null'
                leftColumn = column - 1 if column - 1 >= 0 else 'Null'
                rightColumn = column + 1 if column + 1 <= columns else 'Null'
                # top_element
                if topRow is not 'Null' and grid[topRow][column] == 0 and\
                        (topRow, column):
                    answers.append((topRow, column))
                # bottom_element
                if bottomRow is not 'Null' and grid[bottomRow][column] == 0\
                        and (bottomRow, column):
                    answers.append((bottomRow, column))
                # left_element
                if leftColumn is not 'Null' and grid[row][leftColumn] == 0\
                        and (row, leftColumn):
                    answers.append((row, leftColumn))
                # right_element
                if rightColumn is not 'Null' and grid[row][rightColumn] == 0\
                        and (row, rightColumn):
                    answers.append((row, rightColumn))
    # print('answers array is {}'.format(answers))
    return len(answers)


'''if __name__ == "__main__":
    grid = [
            [0,0,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,1,1,0,0],
            [0,0,0,0,0,0]]
    print(island_perimeter(grid))
'''
