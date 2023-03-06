"""
문제유형: 정렬
문제: https://www.acmicpc.net/problem/1181
풀이
입력받은 리스트에 담은후 sort, sorted 라이브러리는 사용해서 풀이
    1.입력받은 문자 리스트에 append
    2.'중복 제거' -> set() 자료형으로 형변환후 다시 list로 형변환
    3.'길이가 같으면 사전순' -> 전체 문자열 sort로 정렬
    4.'길이가 짧은 것부터' -> sorted 라이브러리에 key매개변수로 객체 길이 함수(len)를 통한 문자열 길이로 정렬

    keypoint : list형 중복 제거시 set로 형변환, 문자열 정렬 라이브러리(sort, sorted) key 매개변수로 함수로 전달 가능!
"""
import sys
input = sys.stdin.readline
n = int(input())

results = []

for _ in range(n):
    word = input().rstrip()
    results.append(word)

results = list(set(results))
results.sort()
print('\n'.join(sorted(results,key=len)))