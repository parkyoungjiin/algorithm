# # -------- 다시 풀면서 잘못 푼 코드 -----------
def solution(X, Y):

    x_dict = {}
    y_dict = {}
    answer = ''
    for i in X:
        # 존재하지 않을 경우 1을 넣어줌.
        if x_dict.get(i) == None:
            x_dict[i] = 1
        else:
        # 존재할 경우 증감처리
            x_dict[i] += 1

    for i in Y:
        # 존재하지 않을 경우 1을 넣어줌.
        if y_dict.get(i) == None:
            y_dict[i] = 1
        else:
            # 존재할 경우 증감처리
            y_dict[i] += 1
# print(x_dict.keys()

    for i in x_dict.keys():
    # key가 y_dict에 존재할 경우 & 0이 아닌 경우
        if i in y_dict and i != '0':
            # min 사용 이유 : x_dict, y_dict에서 적은 횟수가 공통횟수이기 때문에 사용.
            answer += str(str(i) * min(x_dict[i], y_dict[i]))
            # 존재하면서 & 0인 경우 (0인 경우는 1번만 더해야 함.)
        elif i in y_dict and i == '0':
            answer += str(i)
    # 내림차순 정렬하기.
    answer = ''.join(sorted(list(answer),reverse=True))

# key가 y_dict에 존재하지 않을 경우 -1
    if answer == '':
        answer = '-1'

    return answer
    

solution("100","2345")
solution("100","203045")
# solution("100","123450")
# solution("12321","42531")




def solution(X, Y):
    answer = ''
    x_dict = {str(i) : 0 for i in range(10)}
    y_dict = {str(i) : 0 for i in range(10)}

    for x in X:
        x_dict[x] += 1

    for y in Y:
        y_dict[y] += 1

    # print("x_dict:", x_dict)
    # print("y_dict:", y_dict)
    
    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(x_dict[k], y_dict[k])
        answer += k * iternum
        # print(answer)
        # 0이 2번 나오게 되면 0을 하나로 처리해야 함.
        
    if answer == '':
        return "-1"
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer