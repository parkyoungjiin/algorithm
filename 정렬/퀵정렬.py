# 퀵 정렬
# -> 기준 데이터를 설정하고 그 기준보다 큰 데이터, 작은 데이터 위치를 바꾸자
                                                                
# 피벗 = 큰 숫자, 작은 숫자 교환할 때 기준을 피벗.

# 피벗 설정 -> 왼쪽부터는 피벗보다 큰 데이터 (1)/ 오른쪽부터는 피벗보다 작은 데이터 (-1)

array = [5,7,9,0,3,1,6,2,4,8]
 
# def quick_sort(array,start,end):
#     if start>=end:#원소가 1개인 경우
#         return
#     pivot = start #피벗은 첫번째 원소로 설정
#     left = start+1
#     right = end
#     while left<=right:#작은 데이터, 큰데이터 엇갈리지 않은 경우
#         #피벗보다 큰 데이터를 찾을 때까지 오른쪽으로 한칸씩 이동(->)
#         while left<=end and array[left]<=array[pivot]:
#             left+=1
#         #피벗보다 작은 데이터를 찾을 때까지 왼쪽으로 한칸씩 이동(<-)
#         while start<=right and array[right]>=array[pivot]:
#             right-=1
#         if left>right:#엇갈린 경우 작은 데이터와 피벗 교체
#             #작은데이터, 피벗데이터
#             array[right],array[pivot]=array[pivot],array[right]
#         else: #엇갈리지 않았을 경우 작은 데이터와 큰 데이터 교체
#             array[left],array[right]=array[right],array[left]
    
#     #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1,end)
    
# quick_sort(array,0,len(array)-1)
# print(array)

def quick_sort(array):
    if len(array) <= 1:
        return array
    print('arr:',array)
    pivot = array[0]
    tail = array[1:] # 피벗 제외 리스트

    # 피벗보다 작은 값은 왼쪽으로 배치한다.
    left_side = [x for x in tail if x<=pivot]
    # 피벗보다 큰 값은 오른쪽 배치.
    right_side = [x for x in tail if x>pivot]
    print("left_side:",left_side)
    print("right_side:",right_side)

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print("결과:",quick_sort(array))