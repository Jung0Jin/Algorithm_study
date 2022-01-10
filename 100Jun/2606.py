# https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())
graph = [[] * n for _ in range(n+1)] # 경로를 저장하기 위한 2차원 리스트
for _ in range(m): # 총 m개의 간선을 입력받아 경로를 graph에 저장
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [0]*(n+1)
def dfs(start):
    global count
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0: # 들리지 않은 정점이면 dfs()를 이용하여 반복
            dfs(i)
            count += 1

dfs(1)
print(count)