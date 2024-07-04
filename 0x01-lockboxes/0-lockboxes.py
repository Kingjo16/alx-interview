#!/usr/bin/python3
'''Will Solve a Lockboxes.'''


def canUnlockAll(boxes):
    '''A Python code  which will cheak all the boxS AND open'''

    num = len(boxes)
    s_box = set([0])
    un_box = set(boxes[0]).difference(set([0]))
    while len(un_box) > 0:
        box_Idx = un_box.pop()
        if not box_Idx or box_Idx >= num or box_Idx < 0:
            continue
        if box_Idx not in s_box:
            un_box = un_box.union(boxes[box_Idx])
            s_box.add(box_Idx)
    return num == len(s_box)
