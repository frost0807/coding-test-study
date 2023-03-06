# two pointers

N, M = int(input()), int(input())
arr = list(map(int, input().split()))
arr.sort()

i, j = 0, N-1 # 포인터
count = 0 # 정답
while i < j:
    if arr[i]+arr[j] < M: # 두 수의 합이 작으면 i++
        i+=1
    elif arr[i]+arr[j] > M: # 두 수의 합이 크면 j--
        j-=1
    else: # 두 수의 합이 M이면
        count+=1
        i+=1
        j-=1
    print(arr[i]+arr[j],i, j)

print(count)