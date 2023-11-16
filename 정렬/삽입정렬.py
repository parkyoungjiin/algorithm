# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # 앞번지의 값이 더 큰경우 즉 해당 값이 앞에 삽입되야 하는경우.
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)
         