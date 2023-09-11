def solution(id_list, report, k):
    answer = [0] * len(id_list)
    print(answer)
    # print('answer:', answer)
    temp = []
    # 신고 당한 횟수
    declaration_cnt = {i:0 for i in id_list}
    # 신고한 ID.
    declaration_list = {i:[] for i in id_list}

    # 신고 횟수 count 작업.
    for re in report:
        report_id, reported_id = re.split()
        if reported_id in declaration_cnt and reported_id not in declaration_list[report_id]:
            declaration_cnt[reported_id] += 1
            declaration_list[report_id].append(reported_id)
    
    # 신고횟수(reported_id)가 k회 넘어가는 경우 게시물 정지, 신고한(report_id) ID에 메일 발송
    for reported_id, cnt in declaration_cnt.items():
        if cnt >= k:
            # reported_id가 declaration_list(신고한 아이디)에 존재하는 경우 메일 발송.
            temp.append(reported_id)
    # 
    for key, value in declaration_list.items():
        for i in temp:
            if i in value:
                answer[id_list.index(key)] += 1
    
    
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2) # 2,1,1,0