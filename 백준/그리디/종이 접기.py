# 테스트 케이스 받기
T = int(input())

# 종이 정보
paper_list = []
# 종이 정보 받기
for _ in range(T):
    paper_list = input()
    paper_len = len(paper_list)
    # 가운데 기준 인덱스
    center = paper_len // 2
    print("center:",center)
    
    start_idx = 0
    end_idx = paper_len
    
    for i in paper_list:
        # 가운데 인덱스보다 start_idx가 크지 않아야 함.
        if center > start_idx:
            start_idx = int(i)
            end_idx -= 1
            print("start_idx:",start_idx)
            print("end_idx:",end_idx)
            # 같을 경우 NO를 출력.
            # if paper_list[start_idx] == paper_list[end_idx]:
            #     print("NO")
            #     break
            # else:
            


