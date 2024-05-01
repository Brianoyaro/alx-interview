#!/usr/bin/python
def canUnlockAll(boxes):
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
       # print('unlocked: {}'.format(unlocked))
    for val in unlocked:
        if val in range(len(boxes)):
            check[val] = True
    if False in check:
        return False
    else:
        return True
