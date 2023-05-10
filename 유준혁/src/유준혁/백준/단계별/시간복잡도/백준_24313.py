n, m = map(int, input().split())
c = int(input())
g = int(input())
print(1 if n * g + m <= c * g and c - n >= 0 else 0)