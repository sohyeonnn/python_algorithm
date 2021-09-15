#단어 공부

word = input().upper()  #lower()로 해도 맞음
word_list = list(set(word))     #입력받은 문자열에서 중복값을 제거한 리스트를 생성

cnt = []

for i in word_list:             #중복값 제거된 리스트를 반복함
    count = word.count(i)       #입력된 원본 문자열(word)에서 중복값을 제거한 문자의 개수를 count함.
    cnt.append(count)           #빈 cnt리스트에 중복값을 count를 append함
if cnt.count(max(cnt)) >= 2:    #가장 큰 값을 count했을 때 큰값이 2개 이상이면 ? 출력
    print("?")
else:
    print(word_list[cnt.index(max(cnt))].upper())   #큰값이 1개이면 큰값에 해당하는 인덱스의 문자를 대문자로 출력
'''
print((cnt.index(max(cnt))))
-> 가장 많이 입력된 문자의 word_list에서의 위치(index)를 반환함

-> word_list[]로 리스트 출력으로 바꾸면 위치(index)에 해당하는 문자가 .upper해서 출력됨
'''