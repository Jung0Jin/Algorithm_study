# https://www.acmicpc.net/problem/11726

n = int(input())

fn = [0 for _ in range(n+1)]

if n <= 3:
    print(n)
else:
    fn[1] = 1
    fn[2] = 2
    for i in range(3, n+1):
        fn[i] = fn[i-1] + fn[i-2]

    print(fn[i]%10007)