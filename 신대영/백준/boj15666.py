# 내 풀이
from itertools import combinations_with_replacement
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

tmp_res = []
result = set()


def dfs(depth, prev):
    if depth == m:
        t = tuple(tmp_res)
        if t not in result:
            result.add(t)
        return

    for v in num_list:
        if prev <= v:
            tmp_res.append(v)
            dfs(depth + 1, v)
            tmp_res.pop()


dfs(0, 0)
for a in sorted(list(result)):
    print(*a)


# 좋은 풀이
def dfs(x):
    if len(result) == M:
        print(*result)
        return

    for i in range(x, len(num)):
        result.append(num[i])
        dfs(i)
        result.pop()


N, M = map(int, input().split())
num = sorted(set(list(map(int, input().split()))))
print(num)
result = []
dfs(0)

# 라이브러리 사용 풀이
N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())), key=int)
combs = sorted(set(combinations_with_replacement(nums, M)))
print('\n'.join(' '.join(map(str, comb)) for comb in combs))
