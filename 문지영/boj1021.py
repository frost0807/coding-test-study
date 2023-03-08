"""
deque

참고: https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-1021%EB%B2%88-%ED%9A%8C%EC%A0%84%ED%95%98%EB%8A%94-%ED%81%90%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque([0]*N)
for i, n in enumerate(map(int, input().split())): # 뽑을순서저장
    queue[n-1] = i+1

answer=0 # 정답
for i in range(1, M+1):
    idx = queue.index(i) # 뽑을 수의 위치

    if idx <= len(queue)-idx: # left
        for _ in range(idx):
            queue.append(queue.popleft())
            answer+=1
    else: # right
        for _ in range(len(queue)-idx):
            queue.appendleft(queue.pop())
            answer+=1

    queue.popleft() # 뽑기

print(answer)