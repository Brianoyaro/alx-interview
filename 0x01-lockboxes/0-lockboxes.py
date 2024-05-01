#!/usr/bin/python3
"""module solving locked boxes"""


def canUnlockAll(boxes):
    """determines if all boxes can be unlocked"""
    stack = [0]
    unlocked = [0]
    tracker = [0]
    check = [False for i in range(len(boxes))]
    while stack:
        for val in boxes[stack[0]]:
            if val not in tracker:
                stack.insert(len(stack), val)
        for val in boxes[stack[0]]:
            if val not in unlocked:
                unlocked.append(val)
        tracker.append(stack[0])
        stack.remove(stack[0])
    for val in unlocked:
        if val in range(len(boxes)):
            check[val] = True
    if False in check:
        return False
    else:
        return True
