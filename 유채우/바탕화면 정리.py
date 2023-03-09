def solution(wallpaper):
    answer = []
    a = []
    num = 0
    minX = 100
    minY = 100
    maxX = 0
    maxY = 0

    for i in range(len(wallpaper)):
        for j in wallpaper[i]:
            if j == '#':
                a.append([i, num])
            num += 1
        num = 0

    for i in a:
        if minX>i[0]:
            minX = i[0]
        if minY>i[1]:
            minY = i[1]
        if maxX<i[0]:
            maxX = i[0]
        if maxY<i[1]:
            maxY = i[1]


    return [minX, minY, maxX+1, maxY+1]