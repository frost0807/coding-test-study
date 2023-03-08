def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    # list comprehension 사용하여 동일한 크기로 리스트 분할
    divide_list = [score[i:i+m] for i in range(0, len(score), m)]
    for i in range(len(divide_list)):
        if len(divide_list[i]) >= m:
            answer += min(divide_list[i])*m
    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))