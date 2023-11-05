N, S, R = map(int,input().split())

broken = list(map(int, input().split())) # 카약이 손상된 팀 번호
extra = list(map(int, input().split())) # 카약이 남는 팀 번호

result = 0
for i in broken:
    if i+1 in extra:
        broken.remove(i+1)
    elif i-1 in extra:
        broken.remove(i-1)
    else:
        result += 1

print(result)

# ----틀린 풀이----
# N, S, R = map(int,input().split())
# team_list = []
# # 전체 팀
# for i in range(N):
#     team_list.append(i+1)
# # 손상 팀
# lost_team = list(map(int,input().split()))
# # 더 가져온 팀
# surplus_team = list(map(int,input().split()))
# # 손상 팀을 전체 팀에서 제거
# for lost in lost_team:
#     if lost in team_list:
#         team_list.remove(lost)
# # print(team_list)

# # 여분 팀에서 빌려줄 수 있으면 추가
# for surplus in surplus_team:
#     if int(surplus) + 1 not in team_list and (int(surplus) + 1) <= N:
#         team_list.append(int(surplus) + 1)
#         continue
#     if int(surplus) - 1 not in team_list and (int(surplus) -1) > 0:
#         team_list.append(int(surplus) -1)
#         continue

# # print(team_list)
# print(N - len(team_list))

