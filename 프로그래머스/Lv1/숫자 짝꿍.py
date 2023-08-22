def solution(X, Y):
    answer = ''
    x_dict = {}
    y_dict = {}

    for x_i, y_i in X, Y:
        # 존재하지 않을 경우 1을 넣어줌.
        if x_dict.get(x_i) == None:
            x_dict[x_i] = 1
        else:
            # 존재할 경우 증감처리
            x_dict[x_i] += 1


        if y_dict.get(y_i) == None:
            y_dict[y_i] = 1
        else:
            # 존재할 경우 증감처리
            y_dict[y_i] += 1


    for i in x_dict.keys():
        # key가 y_dict에 존재할 경우
        if i in y_dict and i != '0':
            answer += str(str(i) * min(x_dict[i], y_dict[i]))
        elif i in y_dict and i == '0':
            answer += str(i)
        # 내림차순 정렬하기.
        answer = ''.join(sorted(list(answer),reverse=True))

    # key가 y_dict에 존재하지 않을 경우 -1
    if answer == '':
        answer = '-1'
    
    return print(answer)

solution("100","2345")
solution("100","203045")
solution("100","123450")
solution("12321","42531")