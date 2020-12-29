# https://www.acmicpc.net/problem/13904

n = int(input())

task = []
a = 0
d = 0

for i in range(n):
    d_w = list(map(int,input().split()))
    if d_w[0] > d:
        d = d_w[0]
    d_w.append(i)
    task.append(d_w)
task = sorted(task, key= lambda i: (-i[1],i[0]))

p = []
for _ in range(d+1):
    p.append(-1)

for w in task:
    for i in range(w[0],0,-1):
        if p[i] == -1:
            p[i] = w[2]
            a += w[1]
            break

print(a)
