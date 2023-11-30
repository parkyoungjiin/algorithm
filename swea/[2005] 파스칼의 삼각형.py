T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print('#{}'.format(test_case))
    N = int(input())  
    #1. 첫 번째 줄은 항상 숫자 1이다.

    # 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
    circle = []
    # print(circle)
    for i in range(N):
        temp = []
        for j in range(i+1):
        # j가 0이거나 i와 j가 같으면 1을 넣는다.
            if j == 0 or i == j:
                temp.append(1)
        # 아닌 경우는 연산.
            else:
                # 왼쪽 값이 없는 경우는 0 을 더하고
                # 오른쪽 위 값이 없는경우도 0을 더한다.
                # if j-1 > 0 or j+1 < N or i-1 >0:
                temp.append(circle[i-1][j-1] + circle[i-1][j])
                

                # 위의 2개 값을 더하면 된다.
                # -> [i-1][j-1] + [i-1][j]
                # 자신 왼쪽 + 오른쪽 위 숫자
                # 왼쪽 = j-1
                # 오른쪽 위 i = i -1 , j = j+1
        circle.append(temp)
        print(*temp)
