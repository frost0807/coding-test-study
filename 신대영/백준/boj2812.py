"""

"""
n, k = map(int, input().split())
nums = input()

result = []

for num in nums:
    while result and result[-1] < int(num) and k > 0:
        del result[-1]
        k -= 1
    result.append(int(num))

print(''.join(map(str, result)))
