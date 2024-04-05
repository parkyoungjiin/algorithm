import sys
input = sys.stdin.readline

n, m = map(int, input().split())
#듣X
not_hear = set()
#보X
not_see = set()

for i in range(1, (n+m)+1):
    if i <= n:
        not_hear.add(input().rstrip())
    
    else:
        not_see.add(input().rstrip())

result = sorted(list(not_hear.intersection(not_see)))

print(len(result))
for i in result:
    print(i)
