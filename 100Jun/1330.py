# https://www.acmicpc.net/problem/1330

a, b = map(int, input().split())

if a < b:
    print('<')
    exit(0)
elif a > b:
    print('>')
    exit(0)

elif a == b:
    print('==')
    exit(0)
