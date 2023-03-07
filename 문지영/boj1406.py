# 시간초과

import sys
input = sys.stdin.readline

s1 = list(input().strip()) # 커서 앞
s2 = [] # 커서 뒤
M = int(input())

for _ in range(M):
    query = input().strip()

    if query=='L':
        if s1: s2.append(s1.pop()) # s1->s2
    elif query=='D':
        if s2: s1.append(s2.pop()) # s1<-s2
    elif query=='B':
        if s1: s1.pop() # 삭제
    else: # 'P'
        s1.append(query[-1])

s1.extend(reversed(s2))
print(''.join(s1))