# 시간초과

N = int(input())
arr = list(map(int, input().split()))
X = int(input())
nums = [0] * X # 자연수 포함 여부
answer = 0
for n in arr:
    if X-n > 0 and nums[X-n]: # 정답
        answer += 1
    if n < X:
        nums[n] = 1

print(answer)