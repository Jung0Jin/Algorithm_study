# https://www.acmicpc.net/problem/11508

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

k=2
answer = 0

for i in range(n):
    if i == k:
        k+=3
        continue
    answer += nums[i]

print(answer)

