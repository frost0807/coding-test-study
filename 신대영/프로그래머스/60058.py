def check(p):
    # 균형잡힌 괄호 처리 갯수만 맞으면 된다.
    chr1 = 0
    chr2 = 0
    for value in p:
        if "(" == value:
            chr1 += 1
        elif ")" == value:
            chr2 += 1

        # 옳은 괄호인지 확인
        if chr1 < chr2:
            return False
    return True


def solution(p):
    """
    큐를 사용해서 괄호 처리
    """
    answer = ""
    if p == "" or check(p):
        return p
    else:
        chr1 = 0
        chr2 = 0
        u = ""
        v = ""

        # 균형잡힌 괄호 처리 갯수만 맞으면 된다.
        for idx, value in enumerate(p):
            if "(" == value:
                chr1 += 1
            elif ")" == value:
                chr2 += 1

            if chr1 == chr2:
                u = p[:idx + 1]
                v = p[idx + 1:]
                break

        # 올바른 괄호 이면
        if check(u):
            answer = u + solution(v)
        else:
            answer = "(" + solution(v) + ")"
            for s in u[1:-1]:
                if "(" == s:
                    answer += ")"
                else:
                    answer += "("

    return answer
