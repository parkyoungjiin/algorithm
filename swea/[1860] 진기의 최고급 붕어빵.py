tc = int(input())
for t in range(1,tc+1):
    n, m, k = map(int,input().split())
    isPossible = True
    # 손님 정보(정렬)
    customer = sorted(list(map(int, input().split())))

    customer_max = max(customer)
    # 초 배열
    # second_arr = [0 * i for i in range(1, customer_max + 1)]
    idx, bread = 0, 0

    
    
    for i in range(1, customer_max + 1):
        # 만약, 0초에 오는 손님이 있을 경우 붕어빵을 줄 수 없음.
        if customer[0] == 0:
            isPossible = False
            break

        # n초마다 붕어빵 개수 추가
        if i % m == 0:
            bread += k

        if idx < n:
            if i == customer[idx]:
                idx += 1
                if bread > 0:
                    bread -= 1
                else:
                    isPossible = False
                    break
    if isPossible:
        print("#{}".format(t), "Possible")
    else:
        print("#{}".format(t), "Impossible")





