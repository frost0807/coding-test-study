# 직접구현
import sys
input = sys.stdin.readline
n = int(input().rstrip())

chrs_list = [input().rstrip() for _ in range(n)]

for chrs in chrs_list:
    check = 0

    for c in chrs:
        if '(' == c:
            check += 1
        else:
            check -= 1

        if check < 0:
            break

    if check == 0:
        print('YES')
    else:
        print('NO')


# 우수 예제
vps = sys.stdin.readlines()[1:]

for v in vps:
    v = v.rstrip()
    while '()' in v:
        v = v.replace('()', '')

    if v:
        print('NO')
    else:
        print('YES')
