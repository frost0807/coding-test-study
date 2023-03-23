n = int(input())

words = [input() for _ in range(n)]

for word in words:
    for w in word.split():
        print(w[::-1], end=' ')
    print()
