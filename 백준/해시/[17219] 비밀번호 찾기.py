import sys
input = sys.stdin.readline

n, m = map(int,input().split())
pwd = {}
for _ in range(n):
    url, passwd = input().split()
    pwd[url] = passwd

print(pwd)

for _ in range(m):
    url = input().rstrip()
    print(pwd[url])

