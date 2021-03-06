#알파벳 찾기
'''
문제; 알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력; 첫째 줄에 단어 S가 주어진다.
단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력; 각각의 알파벳에 대해서,
a가 처음 등장하는 위치, b가 처음 등장하는 위치,
... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
'''


'''
**문제풀이
문제점1)
- 리스트형식 출력이 아닌데 리스트형식으로 출력하려했음
문제점2)
- 계속 리스트로 접근해서 index, find를 쓸 생각을 못하고 list.append하려했음

*index(), find()함수 공통점
- 0부터 시작한다.
- (찾을 문자열, 시작점, 종료점) 순서로 사용할 수 있다.
 
*find()함수 특징
- 찾을 문자가 없는 경우 -1을 출력한다.
- 리스트, 튜플, 딕셔너리 자료형에서는 사용 불가.
'''

'''
#1) index()함수 사용
import string

S = input()     #자동으로 문자열 처리가 되므로 input()으로 입력받아도 됨
lower_alpha = [i for i in string.ascii_lowercase]       #알파벳 다 입력해서 리스트 만들어줘도 됨


for i in lower_alpha:   #반복문을 돌려 알파벳 26자를 한번 반복한다. 반복문을 도는 i가 s에 속한 문자라면 index값을 출력하고
    if i in S:
        print(S.index(i), end=' ')

    else:       #아니라면 -1을 출력한다
        print(-1, end=' ')
'''


#2) find()함수 사용
s = input()     #영어 소문자 입력받음
alpha = list(range(97, 123))    #아스키코드로 변환한 알파벳 소문자(a~z) 범위

for i in alpha:     #97~123까지
    print(s.find(chr(i)), end=' ')