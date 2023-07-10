"""
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. (차이가 적은 순 정렬, 오름차순)
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다.
정수가 담긴 배열 numlist와 정수 n이 주어질 때 
numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
"""



def solution(numlist, n):
    # n과의 거리를 계산하여 별도 배열에 추가
    answer = []
    result = []
    for i in numlist:
        answer.append(i-n)
    print(answer)

    for i in sorted(answer[:], key=lambda x:[abs(x), -x]):
        result.append(numlist[answer.index(i)])
    return result

solution([1, 2, 3, 4, 5, 6], 4)
solution([10000,20,36,47,40,6,10,7000],30)


test_lambda = lambda x:x+1
print(test_lambda(3))