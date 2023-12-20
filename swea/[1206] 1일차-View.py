T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    res = 0
    for i in range(2, n-2):
        # 현재 건물
        max_height = max(building[i+1], building[i+2], building[i-1], building[i-2])
        if building[i] > max_height:
            res += building[i] - max_height
        else:
            continue
    print("#{} {}".format(test_case, res))


# for test_case in range(1, T + 1):
#     n = int(input())
#     building = list(map(int, input().split()))
#     res = 0
#     for i in range(2, n-2):
#         # 현재 건물
        # if building[i] > building[i+1] and building[i] > building[i+2] and building[i] > building[i-2] and building[i] > building[i-1]:
        #     max_height = max(building[i+1], building[i+2], building[i-1], building[i-2])
        #     res += building[i] - max_height
#         else:
#             continue
#     print("#{} {}".format(test_case, res))


