from itertools import combinations


def get_p_places(place):
    """
        p 위치 찾기
    """
    result = []
    for j in range(5):
        for k in range(5):
            if place[j][k] == 'P':
                result.append((j, k))

    return result


def check_2_dist(palce, a_point, b_point):
    dist = abs(a_point[0] - b_point[0]) + abs(a_point[1] - b_point[1])

    if dist <= 2:
        if dist == 1:
            return False

        if a_point[0] == b_point[0] and palce[a_point[0]][(a_point[1]+b_point[1])//2] != 'X':
            return False
        elif a_point[1] == b_point[1] and palce[(a_point[0]+b_point[0])//2][a_point[1]] != 'X':
            return False
        elif a_point[0] != b_point[0] and a_point[1] != b_point[1]:
            if palce[a_point[0]][b_point[1]] != 'X' or palce[b_point[0]][a_point[1]] != 'X':
                return False

    return True


def solution(places):
    answer = []
    for place in places:
        p_places = get_p_places(place)
        flag = True
        for c_list in list(combinations(p_places, 2)):
            if not check_2_dist(place, c_list[0], c_list[1]):
                flag = False
                answer.append(0)
                break

        if flag:
            answer.append(1)
    return answer
