# https://www.acmicpc.net/problem/1758

n = int(input())
arr = []
answer = 0

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n):
    tip = arr[i]-i

    if tip > 0:
        answer += tip

print(answer)