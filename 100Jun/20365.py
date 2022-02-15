# https://www.acmicpc.net/problem/20365

n = int(input())

b, r = 0, 0

s = input()
for i in range(n-1):
    f = s[i]
    if s[i] == s[i+1]:
        if i == n-2:
            if s[i+1] == 'B':
                b += 1
            else:
                r += 1
    else:
        if f == 'B':
            b += 1
        else:
            r += 1
        if i == n-2:
            if s[i+1] == 'B':
                b += 1
            else:
                r += 1
print(min(b, r)+1)