n = int(input())
nums = list(map(int, input().split()))

result = []

for i in range(n - 1, 0, -1):  # 뒤에서부터 비교
    if nums[i - 1] > nums[i]:  # 앞에 수가 뒤에 수보다 크다면
        for j in range(n - 1, 0, -1):  # 다시 그 앞에 값을 맨 뒤값과 비교
            if nums[i - 1] > nums[j]:  #
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                result = nums[:i] + sorted(nums[i:], reverse=True)
                print(*result)
                exit()

print(-1)
