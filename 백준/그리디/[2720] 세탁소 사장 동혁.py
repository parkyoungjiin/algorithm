# 테스트 케이스 개수
test_case = int(input())

# 잔돈 유형
change_type = [25, 10, 5, 1]
# 테스트 케이스 개수만큼 입력받기.
for i in range(test_case):
    # 잔돈 개수
    change_num = []
    # 잔돈
    change = int(input())
    
    for c in change_type:
        print(change)
        change_num.append(change // c)
        change = change % c
    # 언패킹(*) : 패킹된 변수를 하나씩 풀어준다.
    print(*change_num)
