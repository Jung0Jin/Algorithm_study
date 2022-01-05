# Pythonic Code For Coding Test

Python은 다른 C-Style의 언어 (C, C++, JAVA, ...) 와 다른 특별한 문법이 많다.

다만 코딩테스트를 위해 Python을 사용하거나, 기본적인 문법만 공부하고 사용하는 분들은 Python만의 특유의 문법 (Pythonic 한 코드)을 잘 활용하지 못하는 경우가 많다.

이 자료는 다음과 같은 분에게 추천한다.

1. 파이썬 문법을 알고 있지만 Pythonic한 코드를 작성하는데 어려움을 겪는 분

2. C-Style 언어를 사용하다 코딩테스트를 위해 Python을 사용하는 분

## Unpacking

'''
a, b = map(int, input().split())
'''

이것은 iterable (모든 반복 가능한 객체를 iterable 하다고 한다. 리스트, 튜플, 문자열 등등...) 한 데이터엔 모두 가능한 문법이다.

그런데 이런 상황이 있다.

1. 입력 받은 list에서 첫번째, 마지막 값만 얻고 싶어

2. 입력 받은 list에서 첫번째, 마지막 값만 제외하고 싶어

'''
_list = [1, 2, 3, 4, 5]
first_index, *rest, last_index = _list
print(rest) # 2 3 4
'''

파이썬은 *(asterisk)를 다음과 같은 상황에 사용한다.

1. 곱셈, 거듭제곱

2. List형 컨테이너를 반복해서 확장

3. 가변 인자

4. Unpacking

위에서 rest에 사용한 것은 가변인자다. 즉, 인자의 갯수가 몇개가 될지 확실하지 않을 때 사용하는 거다. first_index와 last_index가 앞과 끝을 가져가면, rest가 나머지를 가져간다.

Unpacking은 뭘까?

'''
_list = [1, 2, 3, 4, 5]
for num in _list:
    print(num, end = ' ') # 1 2 3 4 5
'''

_list내 원소들을 출력하는 평범한 코드다. 그렇다면 이건 어떨까?

'''
_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5
'''

이것을 List Unpacking 이라고 부른다.

사실 list 뿐만 아니라, 컨테이너형 구조에선 모두 적용할 수 있다. 튜플에서도 되고, set에서도 가능하다. Unpacking을 이야기 했으니 다른 이야기를 해보겠다. 이건 어떤가?

'''
a, b, c = [1, 2, 3]
d = a, b, c
print(d) # (1, 2, 3)
'''

저런식으로 하나의 변수에 여러 값을 할당하면 튜플로 묶인다. 위에서 튜플로 Unpacking을 할 수 있다 했으니, 이건 Packing이라고 생각하면 되겠다.

## List Comprehension

파이썬의 꽃 중 하나로, 한국어로는 지능형 리스트 라고도 한다.

먼저 기본형을 보면,

'''
_list = [i for i in range(10)] # 0 1 2 3 4 5 6 7 8 9
'''

이런 구조다.

그렇다면 이건 어떨까? 백준 온라인 저지 1920번 "수 찾기" (http://boj.kr/1920)

'''
import sys
input = sys.stdin.readline

_ = input()
_set = set(map(int, input().split()))
q = input()
_list = list(map(int, input().split()))

print(*[1 if dt in _set else 0 for dt in _list], sep='\n')
'''

'''
square = [[x ** 2 for x in range(3)] for _ in range(3)]
print(square) # [[1, 4, 9], [1, 4, 9], [1, 4, 9]]
'''

코드의 길이를 줄일 수 있다는 장점이 있지만, 너무 길면 가독성을 해친다.

'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]) # [[6], [9]]
'''

추가 예제

'''
_list = [i for i in range(10)] # 1 ~ 10을 담는 리스트

_list = [2 * i for i in range(10)] # 2, 4, 6, ..., 20을 담는 리스트

tmp = [random.randrange(1,, 200) for i in range(100)]
_list = [i for i in tmp if i % 3 == 0] # 주어진 리스트를 받아 3의 배수만 담는 리스트

list_of_tuple = [(i, j) for i in range(100), for j in range(100, 0, -1)]
_list = [(j, i) for i, j in list_of_tuple] # 값이 두개 들어있는 튜플을 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어서 저장

_list = [i if i <= 15 else 15 for i in tmp] # 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장

x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [(i, j) for i in x, for j in y]
'''

## Dictionaty 잘 쓰기

Dictionary와 Set는 Hash Table 구조를 띄고 있다. 그래서 삽입, 삭제, 탐색 연산의 시간복잡도는 O(1)이다.

초보자가 많이 하는 실수가, 값을 찾기 위해 list에서 in을 사용한다는 것이다. 

'''
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(100):
    if i in data:
        print(1)
'''

이럴 땐 set를 사용해야 한다.

'''
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_data_set = set(data)

for i in range(100):
    if i in _data_set:
        print(1)
'''

몇 백만개의 데이터가 있는 set에 약 10만 번 정도의 in 연산을 시행해도 1초도 안 걸리는 시간에 완료하는데, list를 사용하게 되면 몇 시간 이상 걸릴 수 있다.

set의 구조상, 같은 값이 들어올 수 없다.

'''
i_want_to_erase_duplicate_element = [21, 31, 65, 21, 58, 94, 13, 31, 58]
completed_list = list(set(i_want_to_erase_duplicate_element)) # 21, 31, 65, 58, 94, 13

test_list = ['Test', 'test', 'TEST', 'tteesstt']
converted_list = list(set(map(lambda string: string.lower(), test_list))) # test, tteesstt
'''

dictionary는 키와 쌍으로 이루어져 있다.

'''
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = {}

for i in range(len(price)):
    _dict.append((fruit[i], price[i])) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}
'''

혹시 이렇게 하나요? 여기서는 zip에 대해 나옵니다. zip은 각 iterables의 요소들을 모으는 이터레이터를 만든다. 즉, 리스트를 묶어준다는 이야기다. zip은 dictionary를 만들때도 유용하게 쓰인다.

'''
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}
'''

일반적으로 딕셔너리에서 없는 값을 찾으려고 하면 오류가 난다.

'''
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price)) 

print(_dict['strawberry']) # Error!
'''

이걸 회피하기 위해 in 옵션을 사용하면 초보다.

'''
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price)) 

print(_dict.setdefault('strawberry', 0)) # 0
'''

setdefault는 딕셔너리에 값이 있을 땐 해당 값을 리턴하고, 값이 없을 땐 두번째 인자로 넘겨준 값을 추가하고 추가한 값을 리턴한다.

참고로 해당 메소드를 활용한 유사 dictionary가 있다. 이것을 defaultdict라고 부른다.

'''
from collections import defaultdict

movie_review = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]

index = defaultdict(list)

for review in movie_review:
    index[review[0]].append(review[1]) # {'Train to Busan': [4, 4.2, 4.5], 'Clementine': [5, 5], 'Parasite': [4.5]}
'''