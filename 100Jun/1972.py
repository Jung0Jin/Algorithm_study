# https://www.acmicpc.net/problem/1972

while True:
    s = input().rstrip()
    if s == '*':
        break

    for d in range(1, len(s)-1):
        check = set()
        for i in range(len(s)-d):
            pairs = s[i]+s[i+d]
            if pairs in check:
                print(s, 'is NOT surprising.')
                break
            else:
                check.add(pairs)
        else:
            continue
        break
    else:
        print(s, 'is surprising.')