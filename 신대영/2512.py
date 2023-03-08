"""
문제유형: 이분 탐색
문제: https://www.acmicpc.net/problem/2512
풀이
상한액을 이분탐색으로 찾는 문제
    1.최초 상한액은 start 0, end 예산요청 최대값에 중간값으로 상한액 설정 
    2.상한액과 예상요청 금액중 최소값을 총요청 금액으로 합산
    3.총요청 금액이 총예산 금액보다 크면 end 상한액 -1 작으면 start 상한액 + 1
"""
import sys
input = sys.stdin.readline
n = int(input())
budget = list(map(int, input().split()))
m = int(input())

def solution(budget):
    start, end = 0, max(budget)
    
    while start <= end:
        total = 0
        mid = (start + end) // 2
        
        for b in budget:
            total += min(mid, b)
            
        if total > m:
            end = mid - 1
        else:
            start = mid + 1
    print(end)

if sum(budget) <= m:
    print(max(budget))
else:
    solution(budget)