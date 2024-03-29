# https://www.acmicpc.net/problem/11279

import heapq
from sys import stdin

N = int(stdin.readline())
heap = []

for _ in range(N):
    num = int(stdin.readline())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print('0')

    else:
        heapq.heappush(heap, [-num, num])