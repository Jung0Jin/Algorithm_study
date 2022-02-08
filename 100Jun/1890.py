# https://www.acmicpc.net/problem/1890

n = int(input())

field = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dp = [[0] * n for _ in range(n)] # i, j까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1: # 끝에 도달했을 때
            print(dp[i][j])
            break
        current_count = field[i][j]
        # 오른쪽으로 가기
        if j + current_count < n:
            dp[i][j + current_count] += dp[i][j]
        # 아래로 가기
        if i + current_count < n:
            dp[i + current_count][j] += dp[i][j]