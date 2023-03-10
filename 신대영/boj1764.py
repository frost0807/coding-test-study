import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tmp_set = set()

for _ in range(n):
    tmp_set.add(input().rstrip())

result = []

for i in range(m):
    word = input().rstrip()
    if word in tmp_set:
        result.append(word)

print(len(result))
result.sort()
for r in result:
    print(r)
        
    