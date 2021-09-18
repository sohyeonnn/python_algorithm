#그룹 단어 체커; 실버(5)

'''
풀이를 봐도 도대체 뭔소린지 모르겠음
'''


N = int(input())

group_word_len = 0

for k in range(N):
    word = input()
    error = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1]
            if new_word.count(word[i]) > 0:
                error += 1
    if error ==0:
        group_word_len += 1
print(group_word_len)