T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    # dict를 제작하여 점수
    record = {idx: 0 for  idx in range(1, N+1)}
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-','C+', 'C0', 'C-', 'D0']
    for i in range(1, N+1):
        mid, final, homework = map(int,input().split())
        # 점수 계산.
        total_num = (mid * 35) / 100 + (final * 45) / 100 + (homework * 20) / 100
        record[i] = total_num

        record_value = sorted(list(record.values()), reverse=True)
    # 학점당 평점 비율
    num = N // 10
    k_score = record.get(K)
    final_score = record_value.index(k_score) // num

    print("#{}".format(test_case), grades[final_score])
    
    
