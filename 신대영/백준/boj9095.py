from itertools import product
T = int(input())
nums = [1, 2, 3]

result = 0
result_list = []
temp_result = []


def dfs(temp_res):
    global n, result

    if sum(temp_res) == n:
        temp_result.append(temp_res.copy())
        result += 1
        return
    elif sum(temp_res) > n:
        return

    for i in range(1, 4):
        temp_res.append(i)
        dfs(temp_res)
        temp_res.pop()


num_list = [int(input()) for _ in range(T)]

for n in num_list:
    dfs([])
    result_list.append(len(temp_result))
    temp_result = []

for a in result_list:
    print(a)
