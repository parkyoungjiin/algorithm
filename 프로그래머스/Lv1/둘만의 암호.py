def solution(s, skip, index):
    # skip은 제외할 인덱스번호, 
    answer = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in skip:
        if i in alpha:
            alpha = alpha.replace("", i)
    
    print(alpha)

    
        
    return answer
solution("aukksasdew","wbqd",5)