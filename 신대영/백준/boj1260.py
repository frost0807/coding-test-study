from collections import deque
import sys
input = sys.stdin.readline

# n 정점 개수, m 간선의 개수, v 시작 정점
n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드 연결된 노드 정렬
for g in graph:
    g.sort()

# DFS 메서드 정의


def dfs(v):
    # 현재 노드를 방문 처리
    visited_dfs[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(v):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([v])
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        t = queue.popleft()
        print(t, end=' ')
        visited_bfs[t] = True
        # 해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[t]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)


# 정의된 DFS 함수 호출
dfs(v)
print()
bfs(v)
