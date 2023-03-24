n = int(input())
g = [list(input()) for _ in range(n)]

# 우선 갯수 세는 함수부터 만들자
result = 0


def count():
    global result
    for a in range(n):
        count1 = 1
        count2 = 1
        for b in range(1, n):
            if g[a][b] == g[a][b-1]:
                count1 += 1
                result = max(result, count1)
            else:
                count1 = 1

            if g[b][a] == g[b-1][a]:
                count2 += 1
                result = max(result, count2)
            else:
                count2 = 1


# 밑에거랑 변경
for i in range(n):
    for j in range(n-1):
        if g[i][j] != g[i][j+1]:
            # 오른쪽꺼랑 변경
            g[i][j], g[i][j+1] = g[i][j+1], g[i][j]
            count()
            g[i][j], g[i][j+1] = g[i][j+1], g[i][j]
        if g[j][i] != g[j+1][i]:
            # 밑에꺼랑 변경
            g[j][i], g[j+1][i] = g[j+1][i], g[j][i]
            count()
            g[j][i], g[j+1][i] = g[j+1][i], g[j][i]

# 사탕갯수
print(result)
