# def solution(N, stages):
#     answer = []
#     # 실패율 = 스테이지 도달했으나, 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

#     # 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 리턴.
#     # 실패율이 같으면 작은 번호 스테이지가 먼저.
#     # 스테이지 도달한 유저가 없으면 실패율 0
#     # N = 스테이지 개수, stages = 멈춰있는 스테이지 번호

#     total_users = len(stages)
    
#     # 실패 stage 현황
#     stage_dict = {i : 0 for i in range(1,N+1)}

#     # stage 현황 추가
#     for i in stages:
#         if stage_dict.get(i) != None:
#             stage_dict[i] += 1
#         else:
#             continue
#     # 실패율 구하기
#     fail_stage_per = {i:0 for i in stage_dict.keys()}
#     for key, value in stage_dict.items():
        
#         if value != 0:
#         # 실패율 계산
#             fail_percent = value / total_users
#             # 계산 후 인원 감소
#             total_users -= value
#             # 계산 후 해당 키에 실패율을 넣어줌.
#             fail_stage_per[key] = fail_percent
#         else:
#             fail_stage_per[key] = 0 
#     # print(fail_stage_per)
#     test = sorted(fail_stage_per.items(), key = lambda x:x[1],reverse=True)
#     for i in test:
#         answer.append(i[0])
#     return answer


def solution(N, stages):
    total_users = len(stages)
    result = {}
    for stage in range(1, N+1):
        if total_users != 0:
            # 스테이지 별 실패 한 인원을 count
            count = stages.count(stage)
            # 실패율을 바로 계산하여 result에 대입.
            result[stage] = count / total_users
            total_users -= count
        else:
            result[stage] = 0
    # x라는 매개변수를 통해 dict[key] = value 문법을 사용함.
    # -> value값을 key 기준으로 정렬하였음.
    result = sorted(result,key=lambda x : result[x] ,reverse=True)
    print(result)
    
    
        
# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# solution(4, [4,4,4,4,4])
# solution(5, [0,0,0,0])
solution(2, [1, 1, 1, 1])