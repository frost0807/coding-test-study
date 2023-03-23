from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())

queue = deque()

# 큐에 적재
for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    # 맨위에 카드 제거
    queue.popleft()
    # 맨위 카드 맨 밑으로 추가
    queue.append(queue.popleft())

print(queue.pop())
