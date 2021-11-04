# https://www.acmicpc.net/problem/1302

import sys

N = int(sys.stdin.readline())

book_dict = {}

for _ in range(N):
    book = sys.stdin.readline()
    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] += 1

bestseller = max(book_dict.values())

bestseller_list = []

for book, count in book_dict.items():
    if count == bestseller:
        bestseller_list.append(book)

print(sorted(bestseller_list)[0])