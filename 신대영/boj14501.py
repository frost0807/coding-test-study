"""
문제명 : 퇴사
문제 링크: https://www.acmicpc.net/problem/14501
문제 유형: 다이나믹 프로그래밍 (한번 연산한 것은 중복으로 연산하지 않는 프로그래밍)
문제 풀이: 퇴사전일부터 역순으로 근무시 금액 최대값을 구하는 방식으로 처리
        1. 퇴사전날부터 역순으로 최대값 계산
        2. 근무가 가능한 날(해단날짜 + 소요일수 <= 퇴사전날) 이전날짜(i+1) 최대값과 소요일수 이후에 근무날 최대값(i + t) + 현재 금액중 최대값 갱신
        3. 근무하지 않는날은 이전날짜 최대값과 동일하므로 그대로 저장
        4. 최종적으로 마지막 저장된 dp[0] 값이 최대값 출력
"""
import sys
input = sys.stdin.readline

n = int(input())  # 입력받을 일정수
schedule = [list(map(int, input().split()))
            for _ in range(n)]  # 입력한 일정 저장할 2차원 배열 초기화
dp = [0] * (n + 1)  # 해당 일정에 최대값을 저장하는 리스트


def solution(n, schedule):
    # 퇴사전 마지막 일정부터 내려오면서 최대값을 저장하면서 처리
    for i in range(n - 1, -1, -1):
        t = schedule[i][0]  # 소요일수
        p = schedule[i][1]  # 금액

        # 근무하는날 해당날짜 + 소요일수 <= 퇴사전날
        if i + t <= n:
            # 해당 일자에 최대값을 이전 값과 소요일수 이후의 최대값 + 현재 금액중 최대값으로 갱신
            dp[i] = max(dp[i + 1], dp[i + t] + p)
        else:
            # 근무하지 않는날
            dp[i] = dp[i + 1]
    answer = dp[0]
    print(answer)


solution(n, schedule)
