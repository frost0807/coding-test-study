# 내가 정답
n = input()
t_s = 0
# 자릿수 구하는 공식
for i in range(1, len(n)+1):
    t_s += (9*i)*10**(i-1)

result = t_s - (int('9'*len(n)) - int(n)) * len(n)
print(result)

# 좋은 풀이
n = input()
k = 0

for i in range(len(n)):
    k += (int(n)-(10**i)+1)
print(k)
