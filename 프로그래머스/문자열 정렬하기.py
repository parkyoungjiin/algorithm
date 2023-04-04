def solution(my_string):
    answer = []
    my_stringArr = []
    
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer

solution("hi12392")


