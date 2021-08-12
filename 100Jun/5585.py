# https://www.acmicpc.net/problem/5585

money = 1000 - int(input())
coin_types = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coin_types:
    count += money // coin
    money %= coin

print(count)