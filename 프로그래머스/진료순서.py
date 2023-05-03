"""
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한
배열을 return하도록 solution 함수를 완성해주세요.

 """

def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    print(temp) 
    for i in emergency:
        print(i,'번째 인덱스 값', temp.index(i))
        answer.append(temp.index(i)+1)
        
            
               
    return answer

solution([3, 76, 24])


# 처음 한 생각에 대한 풀이
# 1. 배열 하나씩 꺼내서 비교
# - 비교 후 큰 경우 

def solution2(emergency):
    arr = []
    for i in emergency:
        idx = 1
        for j in emergency:
            if i < j:
                idx += 1
        arr.append(idx)
    return arr