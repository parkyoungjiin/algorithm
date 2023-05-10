"""
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 
solution 함수를 완성해주세요.

[1,2,3] , right => [3,1,2]
"""
def solution(numbers, direction):
    answer = []
    if direction == 'right':
        print('right')
        # 마지막 번지에 있는 값이 정답의 첫 번째에 와야 함.
        answer.append(numbers[-1])
        # 이후에 마지막 번지를 제외한 값들이 차례대로 answer에 들어가면 된다.
        for i in numbers[0:-1]:
            answer.append(i)
    else:
        # 왼쪽으로 이동 시 0번지를 제외한 값들이 순차대로 들어간 후 0번지가 마지막에 answer에 들어가면 정답.
        for i in numbers[1:]:
            answer.append(i)
        answer.append(numbers[0])
    return answer

solution([1,2,3],'right') 

"""
        for i in range(0,len(numbers)):
            # i가 배열의 길이와 같을 경우 (즉, 마지막 번지의 값인 경우)
            # -> 첫 번째 값과 바껴야 함.
            # 반대로, i가 마지막 번지가 아닌 경우는 +1 한값을 넣음.
            if i+1 != (numbers):
                # 임시 값 저장.
                temp = numbers[i+1]
                # i+1번지에 i값 저장.
                numbers[i+1] = numbers[i]
                
            else:
                numbers[i] = numbers[0]

arr = [1,2,3,4,4]
for i in arr[0:-1]:
    print('arr의 i값', i)
"""
