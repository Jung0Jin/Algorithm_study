# 꼭 필요한 자료구조 기초

# # 5-1.py 스택 예제
# stack = []

# # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack) # 최하단 원소부터 출력
# print(stack[::-1]) # 최상단 원소부터 출력

# #5-2.py 큐 예제
# from collections import deque

# # 큐(Queue) 구현을 위해 deque 라이브러리 사용
# queue = deque()

# # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue) # 먼저 들어온 순선대로 출력
# queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
# print(queue) # 나중에 들어온 원소부터 출력

# # 5-3.py 재귀 함수 예제
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()

# recursive_function()

# # 5-4.py 재귀 함수 종료 예제
# def recursive_function(i):
#     # 100번째 출력했을 때 종료되도록 종료 조건 명시
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
#     recursive_function(i+1)
#     print(i, '번째 재귀 함수를 종료합니다.')

# recursive_function(1)

# 5-5.py 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))