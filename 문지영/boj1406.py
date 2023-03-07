# 시간초과

import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = []
M = int(input())
N = len(s1)
for _ in range(M):
    query = input().strip()

    if query == 'P': # 추가
        c = query.split()[1]
        s1.append(c)
    if query == 'L' and not s1: # s1->s2
        s2.append(s1.pop())
    elif query == 'D' and not s2: # s2->s1
        s1.append(s2.pop())
    elif query == 'B' and not s1: # 삭제
        s1.pop()

print(''.join(s1 + list(reversed(s2))))