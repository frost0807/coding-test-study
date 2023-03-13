"""
문제유형: 정렬(계수정렬)
문제: https://www.acmicpc.net/problem/2751
풀이 
1.[sorted 라이브러리] 입력받은 정수 리스트에 append한후 sorted()를 사용해서 내림차순 정렬처리
2.[계수 정렬] 조건에 절댓값이 1,000,000보다 작거나 같은 정수로 계수 정렬 힌트를 줌! 
  1) 절대값 정수 개수만큼 [0]으로 채워진 리스트 생성 
  2) 리스트에 입력된 값에 1000000을 더한 인덱스에 1로 업데이트
  3) 리스트에서 1로 업데이트 된 인덱스에서 1000000 빼서 출력

  keypoint : 1000000미만 조건시 계수정렬 생각해 볼것! 느리지만 sorted 라이브러리도 가능
  
"""
# 1.sorted 라이브러리로 풀 경우
import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    a = int(input())
    result.append(a)

for b in sorted(result):
    print(b)


# 2.계수정렬로 풀었울 경우
import sys
input = sys.stdin.readline

n = int(input())
# 절대값 정수 개수만큼 [0]으로 채워진 리스트 생성 
result = [0] * (1000000 * 2 + 1)

# 리스트에 입력된 값에 1000000을 더한 인덱스에 1로 업데이트
for _ in range(n):
    result[int(input()) + 1000000] = 1

# 리스트에서 1로 업데이트 된 인덱스에서 1000000 빼서 출력
print('\n'.join([str(i - 1000000) for i in range(len(result)) if result[i]]))

