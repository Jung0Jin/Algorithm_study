# https://www.acmicpc.net/problem/1106

from sys import maxsize

c, n = map(int, input().split())

# 광고 정보
ad =  [list(map(int, input().split())) for _ in range(n)]

# 적어도 c명을 늘려야 하기에, 고객의 수 최댓값을 더해준다.
dp = [0] + [maxsize] * (c+100)

for cost, customer in ad:
    for cur_customer in range(customer, c+101):
        dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)

print(min(dp[c:c+101]))