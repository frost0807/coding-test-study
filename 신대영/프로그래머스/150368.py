# 완전탐색이 가능한지 확인
from itertools import product  # 중복순열 리이브러리
discounts = [40, 30, 20, 10]  # 할인률 4


def solution(users, emoticons):
    answer = [0, 0]
    temp_answer = [0, 0]
    for sale in list(product(discounts, repeat=len(emoticons))):
        temp_answer = [0, 0]
        for user in users:
            price = 0
            for i in range(len(sale)):
                # 할인률이 높으면 계산
                if sale[i] >= user[0]:
                    price += emoticons[i] * (100 - sale[i]) // 100

            # 계산 금액이 크면 플러스 서비스 가입자 추가
            if price >= user[1]:
                temp_answer[0] += 1
            # 아니면 금액 더해서 처리
            else:
                temp_answer[1] += price

        # 이전 리스트와 비교후 max값을 갱신
        answer = max(answer, temp_answer)

    return answer
