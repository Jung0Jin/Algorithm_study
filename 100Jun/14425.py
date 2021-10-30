# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = {}
count = 0

for i in range(1, N+1):
    word = input().rstrip()
    word_dict[word] = i

for _ in range(M):
    word = input().rstrip()
    if word in word_dict.keys():
        count += 1

print(count)