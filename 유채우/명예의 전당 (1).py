def solution(k, score):
    answer = []
    a = []  # [0,0,0]

    for i in range(len(score)):
        if i < k:
            a.append(score[i])
        else:
            if min(a) < score[i]:
                a.remove(min(a))
                a.append(score[i])
        answer.append(min(a))
    return answer