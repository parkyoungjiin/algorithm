def solution(s):
    answer = 0
    # x와 동일한 횟수, x와 다른 횟수
    x_cnt , x_another_cnt = 0,0
    temp =[]
    for i in s:
        temp.append(i)
        
        if temp[0] == i:
            x_cnt += 1
        else:
            x_another_cnt += 1

        if x_cnt == x_another_cnt:
            # print("같아짐", x_cnt,x_another_cnt)
            for _ in range(x_cnt +x_another_cnt):
                temp.pop()
            x_cnt, x_another_cnt = 0, 0
            answer += 1
            continue
        else:
            continue


            
   
    return print(answer)

solution("banana")
solution("abracadabra")


    # 두 횟수가 동일해지면 반복문 종료
    # if x_cnt == x_another_cnt:
    #     break