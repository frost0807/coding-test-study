"""
문제유형: 백트래킹
문제링크: https://www.acmicpc.net/problem/1182
"""
n, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0
result = []


def dfs_c(k):
    global count  # 최종 결과값 count는 전역변수를 사용하도록 처리
    # 부분수열 합이 s와 일치하거나 부분수열이 존재하면 카운트
    if sum(result) == s and result:
        count += 1

    for i in range(k, len(num_list)):
        result.append(num_list[i])  # 기존 result에서 하나 추가
        dfs_c(i+1)  # 다음 시작점부터 호출하도록 재귀
        result.pop()  # 뒤에서부터 하니씩 제거


dfs_c(0)
print(count)
