def solution(s):
    answer = []
    s_dict = {}
    for index, key in enumerate(s):
        print(key, index)
        # 0 인 경우는 앞에 등장하지 않은 경우.
        if key not in s_dict:
            # 해당 번지 + 1 한 값을 넣어준다.
            answer.append(-1)
            s_dict[key] = index
        # 0 보다 큰 경우 앞에 등장한 경우임.
        else:
            answer.append(index - s_dict[key])
            s_dict[key] = index

    return print("answer:", answer)
solution("banana")
solution("foobar")

