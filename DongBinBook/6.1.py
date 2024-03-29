# 기준에 따라 데이터를 정렬

# # 6-1.py 선택 정렬 소스코드
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i # 가장 작은 원소의 인덱스
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i] # 스와프

# print(array)

# # 6-2.py 파이썬 스와프(Swap) 소스코드
# # 0 인덱스와 1 인덱스의 원소 교체하기
# array = [3, 5]
# array[0], array[1] = array[1], array[0]

# print(array)

# 6-3.py 삽입 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
