
# 큐 라이브러리 사용해서 구현
from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    answer = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5

        cache.append(city)
        if len(cache) > cacheSize:
            cache.popleft()

    return answer

# list 구현
# def solution(cacheSize, cities):
#     cache = []
#     answer = 0

#     for city in cities:
#         city = city.lower()
#         if city in cache:
#             answer += 1
#             cache.remove(city)
#         else:
#             answer += 5

#         cache.append(city)
#         if len(cache) > cacheSize:
#             cache = cache[1:]

#     return answer
