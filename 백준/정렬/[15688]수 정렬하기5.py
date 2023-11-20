import sys
input = sys.stdin.readline

N = int(input())
test_list = []
for _ in range(N):
    test_list.append(int(input()))

[print(i) for i in sorted(test_list)]

# sorted는 새로운 리스트를 반환한다. 문법 : sorted(list, reverse=True/False)
# sort는 반환값이 없음(None) 문법 : list.sort(key=None, reverse=True/False)
# 원본 리스트를 유지하고 싶으면 sorted를 사용해서 정렬한 리스트를 새로 만들면 된다.
# sort()는 원본 리스트를 변경한다.