def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for k in range(4):
                stack.pop()

    return answer



# 시간초과 코드
def findhamburger(ing):
    a = []
    for i in range(len(ing) - 3):
        a = ing[i:i + 4]
        if a == [1, 2, 3, 1]:
            del ing[i:i + 4]
    return ing


def solution(ingredient):
    answer = 0
    while (len(ingredient) >= 4):
        ingredient = findhamburger(ingredient)
        answer += 1

    return answer