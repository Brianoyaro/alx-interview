#!/usr/bin/env python3
"""Pascal triangle interview question"""


def pascal_triangle(n):
    """returns a list of lists of pascal triangle rows"""
    if (n <= 0):
        return []
    if (n == 1):
        return [[1]]
    final_array = [[1], [1, 1]]
    if (n == 2):
        return final_array
    i = 2
    while (i < n):
        temp = final_array[-1]
        value = [1]
        for j in range(len(temp) - 1):
            val = temp[j] + temp[j + 1]
            value.append(val)
        value.append(1)
        final_array.append(value)
        i += 1
    return final_array
