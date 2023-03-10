"""
문제유형: 다이나믹 프로그래밍
문제: https://www.acmicpc.net/problem/11055
풀이
  1.dp 테이블에 입력받은 수열로 초기화
  2.첫번째 기준항 i항 1 ~ n-1 까지 반복하면서 i항값과 이전항값을 비교
  3.i항값 보다 작으면 기존 dp i항값과 dp이전항과 i항 값을 더한값 중 큰값으로 저장
  4.부분수열합 dp테이블에 최대값 출력 
  
  keypoint: 부분수열 나올시 순증가함수 n{k} < n{k+1} 유념할것!
            n = 1000이며, 시간 제한이 1초이므로 대략 O(n^2)시간의 알고리즘을 설계

"""
n = int(input())
array = list(map(int, input().split()))

dp = array[:]

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))

