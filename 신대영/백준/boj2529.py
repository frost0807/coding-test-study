
def dfs(depth, prev):

    if depth == N:
        res_list.append(result.copy())
        return

    if buhos[depth] == ">":
        for a in nums[:prev]:
            if not used[a]:
                result.append(a)
                used[a] = True
                dfs(depth + 1, a)
                result.pop()
                used[a] = False
    else:
        for a in nums[prev + 1:]:
            if not used[a]:
                result.append(a)
                used[a] = True
                dfs(depth + 1, a)
                result.pop()
                used[a] = False


N = int(input())
buhos = list(map(str, input().split()))
used = [False] * 10
nums = [i for i in range(10)]
result = []
res_list = []

# 0 ~ 9 까지 루프 돌면서 처리 첫번째 숫자
for i in nums:
    result.append(i)
    used[i] = True
    dfs(0, i)
    result.pop()
    used[i] = False

print(''.join(map(str, max(res_list))))
print(''.join(map(str, min(res_list))))
