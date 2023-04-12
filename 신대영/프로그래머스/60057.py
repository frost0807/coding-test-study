def solution(s):

    if len(s) == 1:
        return 1

    answer = 10000
    for i in range(1, (len(s) // 2) + 1):
        result = ''
        c = 1
        be_str = s[:i]
        for j in range(i, len(s) + i, i):
            if be_str == s[j:j+i]:
                c += 1
            else:
                if c == 1:
                    result += be_str
                else:
                    result += str(c) + be_str

                be_str = s[j:j+i]
                c = 1

        answer = min(answer, len(result))

    return answer
