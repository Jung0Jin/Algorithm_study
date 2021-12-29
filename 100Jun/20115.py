# https://www.acmicpc.net/problem/20115

n = int(input())
x = list(map(int, input().split()))

x.sort(reverse=True)

answer = 0
for i in range(n):
    if i == 0:
        answer += x[i]
    else:
        answer += x[i]/2

print(answer)