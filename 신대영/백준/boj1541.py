"""
문제유형: 그리디 알고리즘
문제: https://www.acmicpc.net/problem/1541
풀이: 입력받은 수식에서 '-'로 나눠서 첫번째를 제외한 나머지 값을 더해서 빼주면 되는 문제
   1.입력받은 수식 '-'문자로 구분해서 리스트 형태로 도출(split)
   2.해당 리스트 순차적으로 '+'문자 있는지 확인후 값 합산해서 합산 리스트에 저장함
   3.합산 리스트에 첫번째 인자를 제외한 나머지 합산후 빼주면 끝 
"""
import re
expression = re.split('-',input())

result = []

for f in expression:
    if '+' in f:
        plus_nums = list(map(int,f.split('+')))
        result.append(sum(plus_nums))
    else:
        result.append(int(f))

answer = result[0] - sum(result[1::])

print(answer)