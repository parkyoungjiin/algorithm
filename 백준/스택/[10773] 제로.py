import sys
input = sys.stdin.readline

k = int(input())

account_book = []

for _ in range(k):
    n = int(input())

    if n != 0:
        account_book.append(n)
    else:
        account_book.pop(-1)
print(sum(account_book))

