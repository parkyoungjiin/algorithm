# 선택 정렬 : 가장 작은 데이터를 맨 앞으로 보내는 작업을 반복하는 정렬기법(N-1)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        # 가장 작은 데이터 판별
        if array[min_index]> array[j]:
            min_index = j
    #스와프
    array[i], array[min_index] = array[min_index], array[i]


