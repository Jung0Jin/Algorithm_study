# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
input_num = [x for x in range(n)]
# print(input_num)
coin_types = []
for i in input_num:
    coin_types.append(int(input()))

coin_types.sort(reverse=True)

count = 0
for coin in coin_types:
    count += k // coin
    k %= coin

print(count)
