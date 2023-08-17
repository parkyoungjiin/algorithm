def solution(babbling):
    answer = 0
    possible_word = ["aya", "ye", "woo", "ma"]

    # babbling이 possible_word에 있는 지 확인
    for i in babbling:
        for word in possible_word:
            # 2번 연속된 발음은 할 수 없기에 word * 2 not in 을 거쳤음.
            if word * 2 not in i :
                i = i.replace(word, ' ')
        if i.isspace():
            answer += 1

        # if len(i.strip()) == 0:
        #     answer += 1
    

    return answer


solution(["aya", "yee", "u", "maa"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])