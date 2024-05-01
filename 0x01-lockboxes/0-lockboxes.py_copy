#!/usr/bin/python3
"""module representing whether a group ob boxes can be unlocked
"""


def canUnlockAll(boxes):
    """determines if given boxes can be unlocked
    """
    keys = []
    for box in boxes:
        if len(box) == 0:
            keys.append(0)
        else:
            keys.append(box[0])
    unique_keys = list(set(keys))
    if len(unique_keys) == len(boxes):
        return True
    return False
