import sys
input = sys.stdin.readline

n, m= map(int,input().split())


dict = {i:0 for i in range(1, n+1)} 


for i in range(1, n+1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for _ in range(m):
    quiz = input().rstrip()
    if quiz.isdigit():
        print(dict[int(quiz)])
    else:
        # 문자를 주어졌을 때 번호(Key)를 출력
        print(dict[quiz])



