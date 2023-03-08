"""
# deque

참고: https://velog.io/@slbin-park/%EB%B0%B1%EC%A4%80-5430%EB%B2%88-AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()  # 수행할 함수
    n = int(input())
    arr = input().strip()[1:-1].split(',')
    queue = deque(arr)  # 배열
    if n == 0:  # 배열의 길이가 0
        queue = deque()

    count = 0  # 뒤집기 횟수
    error = False  # error인지
    for s in p:
        if s == 'R':
            count += 1
        elif s == 'D':
            if queue:  # 뒤집기가 짝수면 왼쪽에서 버리기
                if count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:  # 빈 queue이면 탈출
                error = True
                break

    if not error:
        if count % 2 != 0: queue.reverse()  # 뒤집기가 홀수면 뒤집기
        print('[' + ",".join(queue) + ']')
    else:
        print('error')