import sys
input = sys.stdin.readline

K, L = map(int, input().split())
student_id = {} # {학번:순서}
for i in range(L):
    sId = input().rstrip()
    # dict에 존재 X -> 값 넣어주기
    if student_id.get(sId) == None:
        student_id[sId] = i
    # dict에 존재하는 경우 -> 순번을 i번째로 변경
    else:
        student_id[sId] = i
        # {key:value} key -> value 

# value 기준 오름차순 정렬
student_id = sorted(student_id.items(), key=lambda x:x[1])
print(student_id)
# K : 수강 가능 인원(10만) , L : 대기 목록 길이 (50만)
for i in range(K):
     # k = 6 
     # 0,1,2,3,4,5 5 -> indexError
     # [('20103324', 0), ('20133221', 2), ('20140101', 4), ('01234567', 5)] len = 4
     
     if i < len(student_id): 
         print(student_id[i][0])
     else: 
         break