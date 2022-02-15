# https://www.acmicpc.net/problem/9498

score = int(input())

if score >= 90:
    print('A')
    exit(0)

elif score >= 80 and score < 90:
    print('B')
    exit(0)

elif score >= 70 and score < 80:
    print('C')
    exit(0)

elif score >= 60 and score < 70:
    print('D')
    exit(0)

else:
    print('F')
    exit(0)