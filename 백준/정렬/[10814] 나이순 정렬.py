# 나이, 이름 (가입순)

# 나이가 같으면 먼저 가입한 사람이 앞으로 오는 순서 정렬 프로그램 작성. + 나이 증가순으로 ( 나이를 기준으로 오름차순 정렬)

import sys
input = sys.stdin.readline
N = int(input())
test_list = []
for i in range(N):
    age,name = map(str,input().split())
    # i를 사용한 이유 -> sort할 때 첫 번째 인덱스 값으로 판별한 후 같을 경우 i(들어온 순서대로 순서가 정해져있음)로 판별하기 위함
    test_list.append([int(age),i,name])

test_list.sort()

for i in range(len(test_list)):
    # 문자열 포맷팅 -> "%자료형" % 값 
    # [i][0] 값은 정수형으로 [i][2] 값은 문자열로 나타내라는 뜻.
    print("%d %s" % (test_list[i][0], test_list[i][2]))
    # print("{0}".format(test_list[i][0]))





