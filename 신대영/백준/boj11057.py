N = int(input())
dp = [1] * 10

# 맨 뒷자리를 기준으로 규칙 찾기
# 맨 뒷자리 수의 경우의 수 + 이전 수의 경우의 수 규칙
for i in range(N-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)
