def solution(s):
    s = sorted(s[2:-2].split('},{'), key=len)

    answer = []
    temp = set()
    for i in range(len(s)):
        ss = (set(s[i].split(',')) - temp).pop()
        temp.add(ss)
        answer.append(int(ss))

    return answer
