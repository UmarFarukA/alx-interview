#!/usr/bin/python3
'''A function definition of canUnlockAll'''


def canUnlockAll(boxes):
    '''This represent the function definition
    that check whether a box can be unlock or not
    parameter:
        boxes (list) - A list of list boxes
    Return:
        True if all boxes can be unlock
        otherwise false
    '''
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
