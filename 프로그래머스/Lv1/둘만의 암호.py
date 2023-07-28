from collections import deque


def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for i in skip:
        if i in alpha:
            alpha = alpha.replace(i, "")

    for i in s:
        if i in alpha:
            s_index = (alpha.index(i) + index) % len(alpha)
            answer += alpha[s_index]
    return answer
    

solution("aukks","wbqd",5)