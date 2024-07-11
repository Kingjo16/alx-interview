#!/usr/bin/python3
'''The coding challenge for operational minimizing'''


def minOperations(n):
    '''compete with a min code'''
    if not isinstance(n, int):
        return 0
    count_op = 0
    clip_or = 0
    final = 1
    while final < n:
        if clip_or == 0:
            # init (the first copy all and paste)
            clip_or = final
            final += clip_or
            count_op += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - final > 0 and (n - final) % final == 0:
            # copy all and paste
            clip_or = final
            final += clip_or
            count_op += 2

        elif clip_or > 0:
            final += clip_or
            count_op += 1
        
    return count_op
