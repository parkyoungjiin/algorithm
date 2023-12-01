import sys 
input = sys.stdin.readline

n = int(input())

a = sorted(list(map(int, input().split())))

m = int(input())

b = list(map(int, input().split()))

for i in b:
    tf = False
    start, end = 0, n-1 
    while start <= end:
        mid = (start + end) // 2
        if i == a[mid]:
            tf = True
            print(1)
            break
        elif i > a[mid]:
            start = mid + 1
        else:
            end = mid -1

    if not tf:
        print(0)
    
        


    



