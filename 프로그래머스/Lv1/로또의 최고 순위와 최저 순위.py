def solution(lottos, win_nums):
    answer = []
    # 알 수 없는 번호 = 0, 구매한 로또 번호 -> lottos
    # 순위
    # 1. 6개 모두 일치 1등, 5개 2등, ... , 2개 일치 5등, 그외 낙첨
    lotto_rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    # 맞은 개수
    lotto_right_cnt, zero_cnt = 0, lottos.count(0)
    # print(zero_cnt)
    for i in lottos:
        if i in win_nums:
            lotto_right_cnt += 1
    print(lotto_rank[zero_cnt + lotto_right_cnt], lotto_rank[lotto_right_cnt])
    return lotto_rank[zero_cnt + lotto_right_cnt], lotto_rank[lotto_right_cnt]
   # 0이 한 개라도 있는 경우
    # if zero_cnt > 0:
    #     lotto_high_cnt = lotto_right_cnt + zero_cnt
    #     answer.append(lotto_rank[lotto_high_cnt])
    #     answer.append(lotto_rank[lotto_right_cnt])
    # else:
    #     answer.append(lotto_rank[lotto_right_cnt])
    #     answer.append(lotto_rank[lotto_right_cnt])



# solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0]	, [38, 19, 20, 40, 15, 25]	)
solution([45, 4, 35, 20, 3, 9]	,[20, 9, 3, 45, 4, 35]	)