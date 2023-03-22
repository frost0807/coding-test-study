"""
"""
score_list = [sum(list(map(int, input().split()))) for _ in range(5)]

result = [0, 0]

for i in range(len(score_list)):
    if result[1] < score_list[i]:
        result[0] = i + 1
        result[1] = score_list[i]

print(' '.join(map(str, result)))
