
def dac(a, b, c):
    if b == 0:
        return a % c
    if b % 2 == 0:
        return (dac(a,b//2,c) ** 2) %c
    else:
        return ()
a, b, c = map(int, input().split())
result = 1
for i in range(b):
    result *= a

print(result%c)