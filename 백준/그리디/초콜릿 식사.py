# 초콜릿
K = int(input())

choco = 1
mod = 0
# 구매해야 하는 가장 작은 초콜릿 구하기
while K > choco:
    choco *= 2
    print(choco)
# 초콜릿 나누기    
while True:
    # 초콜릿을 나눠줄 수 없는 경우(나머지 = 0)
    if K % choco == 0:
        print(mod)
        break
    # 초콜릿을 나눠줄 수 있을 때 
    else:
        choco //=2
        mod += 1


    