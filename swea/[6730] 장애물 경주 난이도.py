T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    hurdle = list(map(int,input().split()))
    up_h, down_h = 0, 0
    for i in range(n-1):
        # 다음 단계가 더 높으면 올라가는 난이도
        if hurdle[i] < hurdle[i+1]:
            up_h = max(up_h, hurdle[i+1] -hurdle[i])
        # 다음 단계가 더 낮으면 내려가는 난이도
        else:
            down_h = max(down_h, hurdle[i] - hurdle[i+1])
    print("#{} {} {}".format(test_case, up_h, down_h))

