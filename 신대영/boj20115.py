"""
문제유형: 그리디 알고리즘
문제: https://www.acmicpc.net/problem/20115
풀이:
"""
n = int(input())
array = list(map(int, input().split()))

array.sort()

for i in range(len(array) - 1):
    if array[i] < array[i + 1]: 
        array[i + 1] = array[i + 1] + (array[i] / 2)
    else:
        array[i + 1] = array[i] + (array[i + 1] / 2)

print(array[len(array) - 1])