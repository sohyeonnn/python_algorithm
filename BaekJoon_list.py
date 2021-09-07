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


