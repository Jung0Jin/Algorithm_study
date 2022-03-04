# https://www.acmicpc.net/problem/2578

bingo = [list(map(int, input().split(' '))) for _ in range(5)]
targets = list()
for _ in range(5):
    targets.extend(list(map(int, input().split())))

visited = [[False] * 5 for _ in range(5)]
row_visited = [False] * 5
col_visited = [False] * 5
x_visited = [False] * 2 # 0: 오른쪽 위, 1: 오른쪽 아래

def ismake_bingo():
    for i in range(5): # row
        if all(visited[i]):
            row_visited[i] = True

    for i in range(5): # col
        temp = list()
        for j in range(5):
            temp.append(visited[j][i])

        if all(temp):
            col_visited[i] = True

    temp_up = list()
    temp_down = list()
    for i in range(5):
        temp_up.append(visited[i][i]) # 오른쪽 아래 대각선
        temp_down.append(visited[i][4-i]) # 오른쪽 위 대각선
    if all(temp_down):
        x_visited[0] = True
    if all(temp_up):
        x_visited[1] = True

def count_bingo():
    count = 0

    for i in range(5):
        if row_visited[i]:
            count += 1
        if col_visited[i]:
            count += 1
    for i in range(2):
        if x_visited[i]:
            count += 1

    return count

for j in range(len(targets)):
    x = None
    for i in range(5):
        if targets[j] in bingo[i]:
            x = i
            break
    y = bingo[x].index(targets[j])

    visited[x][y] = True
    ismake_bingo()
    if count_bingo() >= 3:
        print(j+1)
        break