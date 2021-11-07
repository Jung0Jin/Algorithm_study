# https://www.acmicpc.net/problem/1927

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)