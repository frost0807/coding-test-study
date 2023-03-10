"""
recursion
참고: https://ggasoon2.tistory.com/11

"""
def func(n, r, c):
    if n==0: return 0 # 종료
    half = 2**(n-1)

    if r < half and c < half: # 1사분면
        return func(n-1, r, c)
    elif r < half and c >= half: # 2사분면
        return half*half + func(n-1, r, c-half)
    elif r >= half and c < half: # 3사분면
        return 2*half*half + func(n-1, r-half, c)
    else: # 4사분면
        return 3*half*half + func(n-1, r-half, c-half)

N, r, c = map(int, input().split())
print(func(N, r, c))