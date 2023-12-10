T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    t = int(input())
    print("#{}".format(test_case))
    score_dict = {i:0 for i in range(1, 101)}
    score = list(map(int,input().split()))
    for s in score:
        if s in score_dict:
            score_dict[s] += 1
    # max_count를 통해 최빈값을 저장
    max_count = 0
    for key, value in score_dict.items():
        # 최빈값을 계속 갱신.
        if max_count < value:
            max_count = value
            answer = key
        # 최빈값이 여러개일 때 가장 큰 점수 출력.
        elif max_count == value:
            if answer < key:
                answer = key
    print("#{} {}".format(t, answer))


