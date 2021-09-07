#1546; 평균
'''틀린거,_,
n = int(input())    #과목 수
score = list(map(int, input().split()))
max_score = max(score)

new_score =[]

for i in range(n):
    new_score.append(i/max_score*100)
    new_avg = sum(new_score)/n
print(new_score)
print(new_avg)
'''

'''
n = int(input())    #과목개수
score = list(map(int, input().split()))     #과목별 점수
sum = 0     #sum 0으로 초기화

for i in range(n):     #과목 개수만큼; n대신 len(score) 가능
    sum = sum + score[i] / max(score)       #score input이 for문 안에 있으면 IndexError: list index out of range 에러 발생

print(sum * 100 / n)
'''

#8958; OX퀴즈
'''
문자열 n줄을 입력받아 리스트에 저장할 때
s = [sys.stdin.readline().strip() for i in range(n)]
'''
'''
import sys

n = int(input())

for i in range(n):
    sum_score = 0       #새로운 OX리스트를 입력받으면 점수 합계를 초기화한다.
    score = 0
    OorX = sys.stdin.readline().strip()

    for i in range(len(OorX)):
        if OorX[i] == "O":
            score += 1      #O가 연속되면 점수를 1씩 늘린다.
            sum_score += score  #더해진 score를 sum_score변수에 더한다.

        else:
            score = 0
    print(sum_score)
'''

#4344; 평균은 넘겠지
'''
문제 이해;
student_score_avg를 구함 -> student_score 리스트 안에 있는 수를 모두 더해 student랑 나눈다
student_score_avg < student_score 에 해당하는 값의 개수를 student로 나누고 *100 해준다.

'''
test_case = int(input())

for i in range(test_case):
    student_score = list(map(int, input().split()))
    avg = sum(student_score[1:])/student_score[0]   #student_score[0]은 첫번쩨 입력 즉 입력받을 성적의 수, student_score[1:]는 성적의 갯수 뒤로 입력된 모든 성적을 뜻한다.
    count = 0                           #초기화

    for i in student_score[1:]:         #range(len(student_score))로 해서 오류에서 한동안 못벗어남ㅠㅠ
        if i > avg:                     #i(student_score의 성적들)이 구한 평균값 보다 크다면
            count += 1                  #i 가 평균보다 큰 경우 count변수에 1씩 더해준다.
    per = count/student_score[0] * 100  # (평균보다 더 큰 수의 수/전체)*100

    print("{:.3f} %".format(per))       #format을 활용한 문자열 출력 기억하기

#format 이용해서
# "{:.출력할 소수 자릿수f}출력할 다른 문자열".format(출력변수)
#과 같이 나타낼 수 있다.