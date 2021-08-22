# https://www.acmicpc.net/problem/1439

s = input()
different_num = 0
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        different_num += 1
print((different_num+1)//2)