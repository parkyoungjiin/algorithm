def solution(numbers):
    answer = []
    numbers = sorted(numbers)
    length = len(numbers)
    # numbers에 있는 값을 더해서 만들 수 있는 모든 수를 배열에 오름차순을 담아라.
    for i in range(length):
        for j in range(i+1, length):
            sum_value = numbers[i] + numbers[j]
            # if sum_value not in answer:
            answer.append(sum_value)

    
    return sorted(list(set(answer)))


solution([2,1,3,4,1])
solution([5,0,2,7])

test = set("Hello")
print(test)