def solution(s):
    answer = []
    # 맨 처음 나오면 -1, 아닐 경우는 몇 번쨰 앞에 잇는 지 리턴
    word_dict = {}
    for idx, word in enumerate(s):
        # print(idx, word)
        if word not in word_dict:
            answer.append(-1)
            word_dict[word] = idx
        else:
            answer.append(idx - word_dict[word])
            word_dict[word] = idx


    return answer

solution("banana")