def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
# today변수의 값을 . 기준으로 분류하여 각 변수에 저장.
    today_year, today_month, today_day = map(int, today.split("."))
# 저장한 변수를 일로 변환하였음.
    total_today = (today_year * 12 * 28) + (today_month * 28) + today_day
    #
	
# 약관을 dict에 저장함
    for i in terms:
        terms_dict[i.split()[0]] = i.split()[1]

# privacies 변수 처리 과정
    for index, i in enumerate(privacies):
        privacies_date, term = i.split()
        # print(privacies_date, term)
        privacies_year, privacies_month, privacies_day = map(int, privacies_date.split("."))
        # 약관 종류가 terms_dict에 존재할 경우
        if term in terms_dict:
            privacies_month += int(terms_dict[term])
            if privacies_month > 12:
                privacies_year = privacies_year + (privacies_month // 12)
                privacies_month %= 12
				# terms에 해당하는 개월수를 더한 값을 일로 변환함.
        total_privacies_day = (privacies_year * 12 * 28) + (privacies_month * 28) + privacies_day
        print(total_today, total_privacies_day)
				# 만약, 약관 유효기간이 지난 경우 index 값을 answer에 append.
        if total_today >= total_privacies_day:
            answer.append(index+1)

    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])


# if i.split()[1] in terms_dict:
#             # print(i.split()[1])
#             # print(i.split()[0][5:7])
#             # temp = int(i.split()[0][5:7]) + int(terms_dict[i.split()[1]])
#             # year, month, day = int(i.split()[0].split(".")[0]), int(i.split()[0].split(".")[1]), int(i.split()[0].split(".")[2])
#             month = month + int(terms_dict[i.split()[1]])
#             if month > 12:
#                 month %= 12
#                 year += 1
#             # print(year, month, day)
    
#         if today_year > year and today_month > month and today_day > day:
#             answer.append(index)
        