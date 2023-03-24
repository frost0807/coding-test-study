

def solution(cacheSize, cities):
    cache = []
    answer = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache = cache[1:]

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
#             cache.append(city)
#         else:
#             answer += 5
#             cache.append(city)
#             if len(cache) > cacheSize:
#                 cache = cache[1:]

#     return answer
