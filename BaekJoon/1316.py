#그룹 단어 체커; 실버(5)_문자열,구현
'''
#새로운 풀이 추가
-> 좀 더 직관적임

*point
연속하지 않는 구간에서 문자가 다시 나타나는 경우 그 문자열은 그룹단어가 아님
-> 인덱스 슬라이싱 사용

#이전풀이
마찬가지로 인덱스 슬라이싱을 사용,
차이점: 그룹단어가 아닌것을들 error에 카운트해서  error가 0인 것을 그룹단어로 체크해주는 풀이
'''
#새로운풀이
n = int(input())

result = n

for i in range(n):
    word = input()

    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -= 1
            break
print(result)

'''
#이전풀이
N = int(input())

group_word_len = 0

for k in range(N):
    word = input()
    error = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:    #연달은 두 문자가 나타날 때
            new_word = word[i+1:]   #현재 글자 이후의 문자를 새 문자로 생성한다
            if new_word.count(word[i]) > 0: #새 문자에서 현재 글자가 있었다면
                error += 1  #error에 1 증가(error는 그룹단어가 아닌 문자를 세는 것이다)
    if error ==0:   #error가 0이면 그룹단어이다
        group_word_len += 1
print(group_word_len)
'''