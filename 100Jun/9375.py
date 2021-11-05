# https://www.acmicpc.net/problem/9375

import sys
from collections import Counter

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = []
    for _ in range(n):
        clothes, kind = sys.stdin.readline().split()
        s.append(kind)
    num = 1
    count = Counter(s)
    for key in count:
        num *= count[key] + 1

    print(num - 1)