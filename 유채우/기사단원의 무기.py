def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        count = 0
        for m in range(1, int(i ** (1 / 2)) + 1):  # 1, 2
            if i % m == 0:
                count += 1
                if ((m ** 2) != i):
                    count += 1

        if count > limit:
            count = power
        answer += count
    return answer