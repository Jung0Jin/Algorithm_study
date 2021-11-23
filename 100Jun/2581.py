# https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())

array = []
for i in range(m, n+1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            array.append(i)

if len(array) == 0:
    print(-1)
else:
    print(sum(array))
    print(array[0])