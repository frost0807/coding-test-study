"""
문제유형: 자료구조, 우선순위 큐
문제링크: https://www.acmicpc.net/problem/1927
풀이: 파이썬의 heapq룰 사용해서 최소값을 출력하는 프로그램(heap 자료구조 정리필요)
   1.파이썬 heapq 내장함수 import
   2.음의 정수는 주어지지 않음으로 음수는 배제하고 0일때, 이외에는 자연수로 판단
   3.자연수일 경우 리스트에 추가
   4.0일때 출력시 리스트 존재여부 판단해서 출력
"""
# 입력값이 많을때는 sys.stdin.readline 꼭 추가할것! 아니 무조건 추가해서 문제 풀자!
import sys
input = sys.stdin.readline
# 파이썬 heapq 내장함수 import
# heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공
import heapq  

n = int(input()) # 연산수

# 프로그래머스대비 함수형식으로 문제 풀자
def solution(n):
    heap = [] # 자연수 담은 리스트 초기화
    # 입력받은 값을 통해 출력
    for _ in range(n):
        num = int(input())
        # 음의 정수는 주어지지 않음으로 음수는 배제하고 0일때, 이외에는 자연수로 판단
        if num == 0:  # 0일때
            if heap:  # 리스트 존재하면 최소값 제거후 출력
                print(heapq.heappop(heap))
            else:  # 없으면 0 출력
                print(0)
        else:  # 자연수 일때 리스트에 추가
            heapq.heappush(heap, num)

solution(n)