# 직접 구현 성공
e, s, m = map(int, input().split())

result = 0

# 1~n까지 다 돌면서 확인 15로
result = e

while True:
    # 28로 나눈 나머지가 s랑 동일하면 완료
    if result % 15 == e or (result % 15 == 0 and e == 15):
        if result % 28 == s or (result % 28 == 0 and s == 28):
            if result % 19 == m or (result % 19 == 0 and m == 19):
                break

    result += 15

print(result)

# 우수 풀이
E, S, M = map(int, input().split(" "))
Y = 1
while True:
    if (Y-E) % 15 == 0 and (Y-S) % 28 == 0 and (Y-M) % 19 == 0:
        print(Y)
        break
    Y += 1
