#!/usr/bin/python3
""" lockbox module"""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked using DFS starting from box 0."""
    stack = [0]  # Start with the first box (index 0)
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited
    
    while stack:
        current_box = stack.pop()  # Pop from the stack to perform DFS
        
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                # If the key leads to a valid, unvisited box, mark it as visited and add it to the stack
                visited[key] = True
                stack.append(key)
    
    # Check if all boxes have been visited
    return all(visited)
