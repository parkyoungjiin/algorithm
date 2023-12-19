T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    word = input()
    
    for w in word:
        if w in vowel:
            word = word.replace(w, "")
    print(word)