# https://www.acmicpc.net/problem/19583

import sys

S, E, Q = map(str, sys.stdin.readline().split())

S = int("".join(S.split(':')))
E = int("".join(E.split(':')))
Q = int("".join(Q.split(':')))

attendance = {}

while True:
    line = sys.stdin.readline()
    if len(line) < 5:
        break
    chat_time, name = map(str, line.split())

    chat_time = int("".join(chat_time.split(':')))

    if chat_time <= S:
        attendance[name] = 1
    elif E <= chat_time <= Q:
        if name in attendance:
            attendance[name] += 1

result = 0
for key, value in attendance.items():
    if value >= 2:
        result += 1

print(result)