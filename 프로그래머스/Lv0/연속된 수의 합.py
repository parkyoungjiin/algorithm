"""
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때,
정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
-> 연속된 수의 합이 포인트.
def solution(num, total):
    answer = []
    result = 0
    for i in range(1, total+1): # 12
       for j in range(i, i): # i가 13부터는 total을 벗어난값을 더하기에 안되는 코드.
           result += j
           if result == total:
               for i in range(i, i+num):
                answer.append(i)
               
               break
           else:
               result = 0
    return print(answer)
"""
def solution(num, total):
    answer = []
    avg = total // num
    # print(avg)
    # num = 3, total = 12, avg = 4
    # num = 5, total = 15, avg = 5
    for i in range(avg-1, avg+2):
        print(i)
        
    print("----")
    return answer

solution(3,12)
solution(5,15)
solution(4,14)