def solution(t, p):
    answer = 0
    len_p = len(p)
    a = []
    for i in range(len(t) - len(p) + 1):
        a.append(t[i:i + len_p])

    for s in a:
        if int(s) <= int(p):
            answer += 1

    return answer
