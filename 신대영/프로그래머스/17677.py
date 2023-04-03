"""
    직접구현 정답
"""
from collections import Counter


def solution(str1, str2):
    # 2글자씩 끊어서 다중집합의 원소
    answer = 0
    a = str_div(str1)
    b = str_div(str2)

    ab = set(a) | set(b)

    r_div = 0
    r_add = 0

    for key in ab:
        if key in b and key in a:
            r_div += min(a[key], b[key])
            r_add += max(a[key], b[key])
        elif key in b:
            r_add += b[key]
        else:
            r_add += a[key]

    if r_div == 0 and r_add == 0:
        answer = 65536
    else:
        answer = int(r_div / r_add * 65536)

    return answer

# 문자열 자르는 함수


def str_div(str):
    global aa

    a = {}
    for i in range(len(str) - 1):
        temp_str = str[i:i+2].lower()
        # 특수문자, 공백 제거... 정규표현식으로 하고 싶지만... 생각이 안난다.
        if temp_str[0].isalpha() and temp_str[1].isalpha():
            if temp_str in a:
                a[temp_str] += 1
            else:
                a[temp_str] = 1
    return a


"""
    우수 케이스 
    Counter 함수 사용법 알아두면 좋을듯
"""


def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []

    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])

    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
