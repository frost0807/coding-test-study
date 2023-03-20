"""
문제유형: 정렬, 브루트포스 알고리즘
문제링크: https://www.acmicpc.net/problem/1895
문제풀이: 3 X 3 픽셀을 뽑아서 리스트 정렬을 이용해서 중간값을 도출후 
    1. 가로/세로 시작점을 받아서 3 X 3 픽셀를 루프를 돌면서 값을 도출후 정렬로 중간값을 구하는 함수를 생성
    2. 3 X 3 픽셀이 최대로 움직일수 있는 입력받은 가로/세로 길이에 -2를 해서 루프를 돌면서 중간값 구하는 함수를 호출해서 나오는 값이 비교값(T) 보다 큰 경우 카운트 1씩증가후 출력
"""
R, C = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(R)]
T = int(input())


def solution(R, C, pixel, T):
    count = 0
    for i in range(R - 2):
        for j in range(C - 2):
            if getmiddle(pixel, i, j) >= T:
                count += 1

    print(count)


def getmiddle(pixel, r, c):
    """
    중간값 구하는 함수
    """
    temp_list = []
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            temp_list.append(pixel[i][j])
    temp_list.sort()
    return temp_list[4]


solution(R, C, pixel, T)
