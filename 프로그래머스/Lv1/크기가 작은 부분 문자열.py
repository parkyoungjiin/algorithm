def solution(t, p):
    answer = 0
    len_t, len_p = len(t), len(p)
    # print(len_t, len_p)
    for i in range(len_t):
        # 슬라이싱 후 p와 비교하여 큰지 아닌지 비교함
        # p보다 작거나 같으면 answer += 1
        t_range = i+len_p
        # 슬라이싱할 때 길이가 p와 같아야 카운트를 증가함.
        if t[i:t_range] <= p and len(t[i:t_range]) == len_p:
            # print("확인:",t[i:t_range])
            answer += 1
        else:
            # print("확인:",t[i:t_range])
            continue

    return answer

solution("3141592", "271")
solution("500220839878", "7")
solution("10203", "15")


