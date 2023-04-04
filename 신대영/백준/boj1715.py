import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    num = int(input())
    heapq.heappush(h, num)


result = 0

while len(h) != 1:
    n1 = heapq.heappop(h)
    n2 = heapq.heappop(h)

    result += n1 + n2
    heapq.heappush(h, n1 + n2)

print(result)
