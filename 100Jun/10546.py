# https://www.acmicpc.net/problem/10546

import sys

N = int(sys.stdin.readline())

start_runner = dict()
finish_runner = dict()

for _ in range(N):
    runner = sys.stdin.readline().rstrip()
    if runner in start_runner:
        start_runner[runner] += 1
    else:
        start_runner[runner] = 1

for _ in range(N-1):
    runner = sys.stdin.readline().rstrip()
    if runner in finish_runner:
        finish_runner[runner] += 1
    else:
        finish_runner[runner] = 1

for runner in start_runner.keys():
    if runner not in finish_runner:
        answer = runner
        break
    else:
        if start_runner[runner] != finish_runner[runner]:
            answer = runner
            break

print(answer)