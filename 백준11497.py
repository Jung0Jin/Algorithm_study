# https://www.acmicpc.net/problem/11497

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    result = 0
    for j in range(2,n):
        c = a[j] - a[j - 2]
        result = max(c, result)
    print(result)