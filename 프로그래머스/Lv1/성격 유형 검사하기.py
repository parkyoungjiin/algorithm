def solution(survey, choices):
    answer = ''
    # 점수표 제작
    choices_dict = {i:0 for i in range(1,8)}
    survey_dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(1,8):
        if i > 4:
            choices_dict[i] = i-4
        elif i < 4:
            choices_dict[i] = (i*3) % 4 # 다시 생각하기
    # print(choices_dict)

    for i,j in zip(choices, survey):
        print(i, j)
        if i > 4:
            personal_char = str(j[1])
            survey_dict[personal_char] += choices_dict[i]
        else:
            personal_char = str(j[0])
            survey_dict[personal_char] += choices_dict[i]
    
    # print(list(survey_dict.keys()))
    for i in range(0,len(survey_dict),2):
        first_personal, second_personal = list(survey_dict.keys())[i],list(survey_dict.keys())[i+1]
        if survey_dict[first_personal] > survey_dict[second_personal]:
            answer += first_personal
        elif survey_dict[first_personal] < survey_dict[second_personal]:
            answer += second_personal
        else:
            # 같을 경우는 알파벳순.
            answer += min(first_personal, second_personal)
    


    return answer

solution(["AN", "CF", "MJ", "RT", "NA"]	, [5, 3, 2, 7, 5])
solution(["TR", "RT", "TR"]	, [7, 1, 3])