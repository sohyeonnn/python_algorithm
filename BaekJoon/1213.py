#팰린드롬 만들기(실4)_문자열
'''
주어진 단어를 가지고 팰린드롬 문자를 만드는 문제
-> 만들 수 있다면 만들어진 팰린드롬 문자를 출력
-> 만들 수 없다면 im sorry hansoo를 출력

*point
팰린드롬을 만들기 위해서는 각 알파벳이 짝수개만 존재하거나,
단 1종류의 알파벳만 홀수개로 존재해야 한다.

*point
ord(), chr(), 리스트인덱싱을 적절히 활용해서 풀어야함
'''

import sys
input = sys.stdin.readline

names = list(map(str, input().rstrip()))    #단어 입력받음
name_count = [0 for _ in range(26)]     #0~25의 리스트 생성

for name in names:      #AABBB 를 A,A,B,B,B로 나눠서
    name_count[ord(name)-65] += 1   #아스키코드로 변환한 값-65 (-> A의 경우 0이 됨 즉 0번째 인덱스에 count)을 각각 0~25에 count해줌


odd = 0     #홀수 갯수 셀 변수
odd_list = ''   #홀수 단어 저장할 변수
alpha = ''  #나머지 alpha저장할 변수
for i in range(26):     #0~25
    if name_count[i] % 2 != 0:      #name_count[i]의 값이 홀수라면
        odd += 1    #odd에 1을 더한다
        odd_list += chr(i+65)   #홀수개수인 원소를 odd_list에 해당 원소의 값을 문자 형태로 추가한다( 0번째 인덱스인 경우 경우 0+65는 A이므로 A가 추가되는 것
    alpha += chr(i+65) * (name_count[i]//2)     #홀수개수가 아닌 원소는 입력의 절반만큼 alpha에 넣어준다.


if odd >= 2:
    print("I'm Sorry Hansoo")   #odd가 2개 이상이라면 팰린드롬이 될 수 없다.
else:
    print(alpha + odd_list + alpha[::-1])   #alpha를 앞, 뒤(역순)으로 배치하고 가운데에 홀수인 문자를 두어 출력한다.(=팰린드롬형태)