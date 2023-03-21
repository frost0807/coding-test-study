"""
문제유형: 그리디 알고리즘
문제: https://www.acmicpc.net/problem/20115
풀이: 에너지 드링크를 최대로 남기려면 버리는 양을 최소로 하기위해 입력된 드링크중에 작은양의 드링크를 버리면서 남기는 최선 
   1.입력된 드링크양의 리스트를 내림차순으로 정렬(처음에는 오르차순으올 했으나 검증결과 내림차순으로해야 최적으로 처리됨)
   2.내림차순으로 정렬된 리스트를 순차적으로 돌면서 드링크양을 비교하면선 계산
"""
n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)

for i in range(len(array) - 1):
    if array[i] < array[i + 1]: 
        array[i + 1] = array[i + 1] + array[i] / 2
    else:
        array[i + 1] = array[i] + array[i + 1] / 2

print(array[len(array) - 1])