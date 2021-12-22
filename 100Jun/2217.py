# https://www.acmicpc.net/problem/2217

N = int(input()) # 로프의 수
w = [] # 각 로프의 최대 중량
for _ in range(N):
    w.append(int(input()))
w.sort(reverse=True)

temp = []
for i, v in enumerate(w):
    temp.append((i+1) * v)
print(max(temp))