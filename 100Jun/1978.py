# https://www.acmicpc.net/problem/1978

import sys
input = sys.stdin.readline

n = int(input())
numbers = map(int, input().split())

count = 0
for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            count += 1

print(count)