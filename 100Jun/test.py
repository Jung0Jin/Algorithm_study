n = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return sol(n-1) + sol(n-2)

print(sol(n) % 10007)