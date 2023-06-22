"""
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
   동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
   같은 식이라면 가장 짧은 수식을 return 합니다.


"""

def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x, num =0,0
    for i in polynomial:
        if 'x' in i:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[0])
            
        else:
            num += int(i)
            
    if num > 0:
        answer = str(x) + "x + " + str(num)
    elif x == 1 and num > 0:
        answer = "x + " + str(num)
    elif x == 1 and num == 0:
        answer = "x"
    elif num == 0:
        answer = str(x) + "x"

        
    return print(answer)

solution("3x + 7 + x")
solution("x + x + x")
solution("x + 7")