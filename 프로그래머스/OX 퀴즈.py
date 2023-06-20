"""
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다. 
단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.

"""

def solution(quiz):
    answer = []
    answer_arr = []
    
    for i in range(len(quiz)):
        # 공백 기준으로 첫 번째 연산을 분리하여 배열에 넣음.
        answer_arr = quiz[i].split()
        if answer_arr[1] == '+':
            if int(answer_arr[4]) == int(answer_arr[0]) + int(answer_arr[2]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(answer_arr[4]) == int(answer_arr[0]) - int(answer_arr[2]):
                answer.append('O')
            else:
                answer.append('X')
        
    return print(answer)

solution(["3 - 4 = -3", "5 + 6 = 11"])