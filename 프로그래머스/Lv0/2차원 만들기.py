"""
정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.

num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다.
2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.



"""

def solution(num_list, n):
   cnt = 0 
   answer = []
   temp = []
   # 2개씩 임시배열에 넣기
   for i in num_list:
      temp.append(i)
      cnt += 1
      if cnt == n:
         answer.append(temp)
         temp = []
         cnt = 0
   return print(answer)

    
solution([1,2,3,4],2)

# 다른 풀이(len, range 이용)
def solution2(num_list, n):
   for i in range(0, len(num_list), n):
      print(i)


solution2([1,2,3,4],2)