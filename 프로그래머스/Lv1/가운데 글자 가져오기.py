def solution(s):
    answer = ''
    s_len = len(s)
    # 홀수인 경우
    if s_len % 2 == 1:
        return s[s_len // 2]
    # 짝수인 경우
    else:
        return s[(s_len // 2 -1) : (s_len//2 +1)]
    return answer