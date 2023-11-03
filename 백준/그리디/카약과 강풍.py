N, S, R = map(int,input().split())
team_list = []
# 전체 팀
for i in range(N):
    team_list.append(i+1)
# 손상 팀
lost_team = list(map(int,input().split()))
# 더 가져온 팀
surplus_team = list(map(int,input().split()))
# 손상 팀을 전체 팀에서 제거
for lost in lost_team:
    if lost in team_list:
        team_list.remove(lost)
# print(team_list)

# 여분 팀에서 빌려줄 수 있으면 추가
for surplus in surplus_team:
    if int(surplus) + 1 not in team_list and (int(surplus) + 1) <= N:
        team_list.append(int(surplus) + 1)
    elif int(surplus) - 1 not in team_list and (int(surplus) -1) > 0:
        team_list.append(int(surplus) -1)

print(team_list)
print(N - len(team_list))
# 손상된 팀에 여분으로 가져온 팀이 있는 지 확인
# for index in range(len(lost_team)):
#     if lost_team[index] in surplus_team:

# 빌려줄 수 있는 지 확인.
# for surplus in surplus_team:
#     if int(surplus) + 1 in lost_team:
#         answer += 1
#     else:
#         continue




