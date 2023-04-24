from heapq import *


def solution(m, musicinfos):
    answer = ''
    arr = []
    m = m.replace("C#", 'c')
    m = m.replace("D#", 'd')
    m = m.replace("F#", 'f')
    m = m.replace("G#", 'g')
    m = m.replace("A#", 'a')
    for i in musicinfos:

        s, e, t, mu = [j for j in i.split(",")]

        mu = mu.replace("C#", 'c')
        mu = mu.replace("D#", 'd')
        mu = mu.replace("F#", 'f')
        mu = mu.replace("G#", 'g')
        mu = mu.replace("A#", 'a')

        #####시간구하기
        s_h, s_m = [int(j) for j in s.split(":")]
        s_h = s_h*60
        s_total = s_h + s_m

        e_h, e_m = [int(j) for j in e.split(":")]
        e_h = e_h*60
        e_total = e_h + e_m
        playtime = e_total - s_total

        ####반복 횟수
        iterr = playtime//len(mu)
        res = playtime%len(mu)

        result = (mu*iterr) + mu[:res]

        if m in result:
            heappush(arr, (-playtime, t))

    if arr:
        a = heappop(arr)
        answer = a[1]
    else:
        answer = "(None)"
    return answer
