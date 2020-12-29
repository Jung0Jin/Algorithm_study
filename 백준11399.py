# https://www.acmicpc.net/problem/11399

n = int(input())
list_pi = list(map(int, input().split()))
list_pi.sort(reverse=True)

withdraw = []
for i in range(n):
    # print(i+1, list_pi[i])
    withdraw.append((i+1) * list_pi[i])

print(sum(withdraw))