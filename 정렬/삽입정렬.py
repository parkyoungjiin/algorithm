# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

# 1인 이유 : 삽입의 경우에 첫 번째 자리는 정렬이 된 상태이기 때문.
for i in range(1, len(array)):
    # j : 삽입하고자 하는 원소의 위치
    for j in range(i, 0, -1):
        # 왼쪽 데이터와 비교했을 때 j번째 데이터가 작다면 
        if array[j] < array[j-1]:
            array[i], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춘다.
            break
