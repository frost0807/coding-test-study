"""
문제유형:
문제링크:
문제풀이:
"""
R, C = map(int, input().split())

pixel = [list(map(int, input().split())) for _ in range(R)]
# fillter_pixel = [[0] * (C - 2) for _ in range(R - 2)]
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
    미들 구하는 함수
    """
    temp_list = []
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            temp_list.append(pixel[i][j])
    temp_list.sort()
    return temp_list[4]


solution(R, C, pixel, T)
