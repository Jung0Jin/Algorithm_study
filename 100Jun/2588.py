# https://www.acmicpc.net/problem/2588

a = int(input())
word = input()
d, c, b = int(word[0]), int(word[1]), int(word[2])

print(a*b)
print(a*c)
print(a*d)
print((a*b) + (a*c*10) + (a*d)*100)