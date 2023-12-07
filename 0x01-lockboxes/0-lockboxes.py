#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    checks if all boxes can be unlocked
    Args:
        boxes: a list of list representing the boxes and their keys
    Return:
        Returns true if all boxes can be unlocked. Otherwise false
    """

    keys = {0}
    for box in range(0, len(boxes)):
        if box in keys:
            keys.update(boxes[box])
            for key in boxes[box]:
                if key < len(boxes):
                    keys.update(boxes[key])
        else:
            return False
    return True
