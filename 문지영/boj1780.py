"""
recursion

참고: https://fre2-dom.tistory.com/412
"""
import sys
input = sys.stdin.readline


def func(x, y, n):
    check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != check: # 9개로 자르기
                for a in range(3):
                    for b in range(3):
                        func(x+a * n//3, y+b * n//3, n//3)
                return

    count[check]+=1 # 종이 세기

N = int(input())
board = [] # 종이
for _ in range(N):
    board.append(list(map(int, input().split())))
count = {-1:0, 0:0, 1:0} # 종이 개수
func(0,0,N)
print(*count.values(), sep='\n')