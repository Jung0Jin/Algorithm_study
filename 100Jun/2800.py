# https://www.acmicpc.net/problem/2800

import sys
import itertools

expression = list(map(str, sys.stdin.readline().strip()))
stack, pos, answer = [], [], set()

for idx, value in enumerate(expression):
    if value == '(':
        stack.append(idx)
    if value == ')':
        pos.append((stack.pop(), idx))

for i in range(1, len(pos)+1):
    comb = itertools.combinations(pos, i)
    for j in comb:
        temp = expression[:]
        for s, e in j:
            temp[s] = ''
            temp[e] = ''
        answer.add(''.join(map(str, temp)))
for i in sorted(list(answer)):
    print(i)