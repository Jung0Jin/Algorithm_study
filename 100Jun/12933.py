# https://www.acmicpc.net/problem/12933

duck = input()
visited = [False] * len(duck)
count = 0

if len(duck) % 5 != 0:
    print(-1)
    exit()

def solve(start):
    global count
    quack = 'quack'
    j = 0
    first = True
    for i in range(start, len(duck)):
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = True
            if duck[i] == 'k':
                if first:
                    count += 1
                    first = False
                j = 0
                continue
            j += 1

for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        solve(i)

if not all(visited) or count == 0:
    print(-1)
else:
    print(count)