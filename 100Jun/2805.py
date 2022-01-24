# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) # 이분 탐색 범위 설정

while start <= end: # 벌목 높이 찾기
    mid = (start+end) // 2
    count = 0
    for height in tree:
        if height >= mid:
            count += height - mid

    # 벌목 높이 이분 탐색
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
