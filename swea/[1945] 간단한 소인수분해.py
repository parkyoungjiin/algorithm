# swea는 테스트 케이스를 입력받아주기에 N을 받을 필요 없음.
N = int(input())

for i in range(N):
    # 정수 입력받기.
    num = int(input())
    # 소인수
    prime_number = [2,3,5,7,11]
    # 개수 체크
    check_list = [0,0,0,0,0]
    for index in range(len(prime_number)):
        while num % prime_number[index] == 0:
            check_list[index] += 1
            num //= prime_number[index]
    print('#{}'.format(i+1),' '.join(map(str, check_list)))


