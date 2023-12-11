# 최대 최소를 제외한 나머지 평균값 구하기
# 소수점 첫쨰 자리에서 반올림한 정수 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    value_list = list(map(int,input().split()))
    value_list.remove(max(value_list))
    value_list.remove(min(value_list))
    sum_value = 0
    for value in value_list:
        sum_value += value
    # round(value) : 소수 첫째자리에서 반올림
    # round(value,1) : 소수 둘째자리에서 반올림
    answer = round(sum_value / len(value_list))
    print("#{}".format(test_case), answer)
