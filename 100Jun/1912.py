# https://www.acmicpc.net/problem/1912

n = int(input())
num_list = list(map(int, input().split()))

sum_list = [num_list[0]]
for i in range(len(num_list)-1):
    sum_list.append(max(sum_list[i] + num_list[i+1], num_list[i+1]))
print(max(sum_list))
