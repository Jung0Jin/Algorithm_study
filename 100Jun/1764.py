# https://www.acmicpc.net/problem/1764

n, m = map(int, input().split())

name_list1 = set()
for _ in range(n):
    name_list1.add(input())

name_list2 = set()
for _ in range(m):
    name_list2.add(input())

name_list = sorted(list(name_list1 & name_list2))

print(len(name_list))
for name in name_list:
    print(name)
