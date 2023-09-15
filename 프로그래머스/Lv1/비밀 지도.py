def solution(n, arr1, arr2):
    answer = []

    for ar1, ar2 in zip(arr1, arr2):
        new_arr = bin(ar1 | ar2)
        # zfill 함수 -> n이라는 자리수에 맞게 빈 문자열을 0으로 채워줌.
        new_arr = new_arr[2:].zfill(n)
        new_arr = new_arr.replace("1","#").replace("0"," ")

        answer.append(new_arr)

            
    return answer
#['######', '###  #', '##  ##', '#### ', '#####', '### # ']
#["######","###  #","##  ##"," #### "," #####","### # "]
# solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])

