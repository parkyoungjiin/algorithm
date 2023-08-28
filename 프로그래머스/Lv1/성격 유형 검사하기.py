def solution(survey, choices):
    answer = ''
    # 점수표 제작
    choices_dict = {i:0 for i in range(1,8)}
    for i in range(1,8):
        if i > 4:
            choices_dict[i] = i-4
        elif i < 4:
            choices_dict[i] = (i*3) % 4 # 다시 생각하기
    print(choices_dict)
    survey_dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

        


    return answer

solution(["AN", "CF", "MJ", "RT", "NA"]	, [5, 3, 2, 7, 5])