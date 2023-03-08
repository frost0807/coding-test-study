def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] % 2 == 0:  # 짝수
            for a in range(food[i] // 2):
                answer += str(i)
        else:  # 홀수
            num_food = food[i] - 1
            for b in range(num_food // 2):
                answer += str(i)

    answer += '0'

    for i in range(len(food) - 1, 0, -1):
        if food[i] % 2 == 0:  # 짝수
            for a in range(food[i] // 2):
                answer += str(i)
        else:  # 홀수
            num_food = food[i] - 1
            for b in range(num_food // 2):
                answer += str(i)

    return answer