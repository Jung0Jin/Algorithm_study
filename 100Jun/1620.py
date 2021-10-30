# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pkm_dict = {} # 포켓몬 이름과 번호 저장할 dict

for i in range(1, N+1):
    pkm = input().rstrip()
    pkm_dict[i] = pkm
    pkm_dict[pkm] = i

for _ in range(M):
    word = input().rstrip()
    if word.isdigit():
        print(pkm_dict[int(word)])
    else:
        print(pkm_dict[word])