# two pointers

N = int(input())
start, end = 1, 1 # 포인터
sum = 1
count = 1 # 자기자신 포함

while end < N:
    if sum == N: # 연속된 합이 N이면
        end+=1
        sum+=end
        count+=1
    elif sum < N: # 연속된 합이 N보다 작으면
        end+=1
        sum+=end
    else: # 연속된 합이 N보다 크면
        sum-=start
        start+=1

print(count)