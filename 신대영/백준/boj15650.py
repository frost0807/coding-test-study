from itertools import combinations

n, m = int(input())


def gen_combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in gen_combinations(rest_arr, n-1):
            result.append([elem]+C)

    return result


def solution(n, m):
    l = [i for i in range(1, n + 1)]
    # python 라이브러리 사용 조합
    print(combinations(l, m))
    # python 조한 함수 구현
    print(gen_combinations(l, m))


solution(n, m)
