"""

"""
n, k = map(int, input().split())
nums = input()

result = [0]

for num in nums:
    if result[-1] > num:
        del result[-1]
    else:
        result.append(num)

print(result)
