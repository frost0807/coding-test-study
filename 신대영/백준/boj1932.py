N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]

print(max(dp[N - 1]))
