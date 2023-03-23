import sys
input = sys.stdin.readline

n = int(input())

words = list(input() for _ in range(n))
result = len(words)
for a in words:
    temp = {}
    for i in range(len(a)):
        if a[i] in temp:
            if not a[i-1] == a[i]:
                result -= 1
                break
        else:
            temp[a[i]] = 0

print(result)


# 우수한 풀이 방법
# N = int(input())
# for i in range(N):
#     a = input()
#     if list(a) != sorted(a, key=a.find): # sorted key에 find 항수를 사용하면 해당 문자 존재하면 그 문자 뒤에 정렬되서 처리
#         N -= 1
# print(N)
