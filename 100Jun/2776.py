# https://www.acmicpc.net/problem/2776

import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())

    temp = sys.stdin.readline().split()
    note_dict = {}

    for num in temp:
        note_dict[num] = 1

    M = int(sys.stdin.readline())

    temp2 = sys.stdin.readline().split()

    for num in temp2:
        try:
            print(note_dict[num])
        except:
            print(0)