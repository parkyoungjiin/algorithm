"""
얀에서는 매년 달리기 경주가 열립니다. 
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다.
 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 
해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때,
 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.


"""
def solution(players, callings):
    p_idx_result = {player : i for i, player in enumerate(players)} # 선수 : 등수
    idx_p_result = {i : player for i, player in enumerate(players)} # 등수 : 선수

    # 결과 도출 시 선수명을 출력해야 함.
    for i in callings:
    #     # 호명되면 등수 -1
    #     # 호명된 선수 등수와 이름 + 호명된 선수 앞 선수의 등수와 이름 저장
    #     cur_idx = p_idx_result[i]
    #     cur_player = i
        
    #     # 호명된 선수의 앞 선수 등수와 이름
    #     pre_idx = cur_idx - 1
    #     pre_player = idx_p_result[pre_idx]

    #     # 선수의 등수를 바꿔주는 작업
    #     p_idx_result[cur_player] = pre_idx
    #     p_idx_result[pre_player] = cur_idx

    #     # 등수 : 선수에서 선수명을 변경함.
    #     idx_p_result[pre_idx] = cur_player
    #     idx_p_result[cur_idx] = pre_player


    # return list(idx_p_result.values())

     pla_dic = {key: i for i, key in enumerate(players)} # 선수 : 등수
    print(pla_dic)
    for p in callings:
        index = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[index-1]] += 1
        players[index-1], players[index] = players[index], players[index-1]

    return print(players)

        

    # for i in callings:
    #     if i in players:
    #         index = players.index(i)
    #     # print("i값의 인덱스:", index)
    #     players[index], players[index-1] = players[index-1], players[index]
    # print(players)
    # 스왑하여 리스트 위치 변경하기
    
    
solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
    
    
