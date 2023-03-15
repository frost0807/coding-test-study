a,b,c = map(int, input().split())

rslt = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,end=' ')
            print(j,end=' ')
            print(k,)
            rslt += 1

print(rslt)