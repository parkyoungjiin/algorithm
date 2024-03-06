
# TC = 10 고정이기에 11로
for i in range(1, 11):
    tc = int(input())
    arr = list(map(int,input().split()))

    # -1번지가 0보다 작은 경우까지 반복
    while arr[-1] > 0:
        # 1~5 값을 빼서 마지막 번지로 이동.
        for i in range(1,6):
            num = arr.pop(0)
            arr.append(num - i)
            # -1번지 값이 0이거나 0보다 작은 경우 0으로 만들고 탈출.
            if arr[-1] <= 0:
                arr[-1] = 0
                break

    print("#{}".format(tc), *arr)


                
            





