"""
문제유형: 이분 탐색
문제: https://www.acmicpc.net/problem/2417
풀이
이분 탐색으로 제곱근 구하는 문제로 이분 탬색에 대해 이해가 있어야 풀수 있음
    1.이분탐색 start 0, end 입력받은 수 설정
    2.반복 조건으로 시작시점이 종료시점보다 작거나 같을때까지 수행(이조건 중요!)
    3.중간값의 제곱이 작으면 start에 중간값 + 1 처리 아닐경우 end에 중간값 -1
    4.마지막 start가 end를 넘어갈때의 값이 결과값

    keypoint: 가장 작은 정수를 구하는 것으로 제곱근에 수에 기준이 start가 end 수를 초과하는 시점이 키포인트
"""
n = int(input())
start, end = 0, n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)