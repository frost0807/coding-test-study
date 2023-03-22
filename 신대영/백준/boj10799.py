import sys
input = sys.stdin.readline
s = input().rstrip()

answer = 0
temp = []
for i in range(len(s)):
    # 레이저
    if '(' == s[i]:
        temp.append(s[i])
    else:
        temp.pop()
        if '(' == s[i-1]:
            answer += len(temp)
        else:
            answer += 1

print(answer)
