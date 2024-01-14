#!/usr/bin/python3
"""Check if all boxes (list of lists array where each element is a box
containing keys to other elements) are unlocked"""


def canUnlockAll(boxes):
    # first box is unlocked
    unlocked_boxes = {0}

    # available keys in the firt box
    keys = boxes[0]

    while keys:
        key = keys.pop()

        if key not in unlocked_boxes and key < len(boxes):
            unlocked_boxes.add(key)
            keys.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)
