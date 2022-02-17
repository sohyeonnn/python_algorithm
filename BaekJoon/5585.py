#거스름돈(브2)-그리디
'''
*point
- 거스름돈 개수가 가장 적게 잔돈을 준다.
'''

import sys
input = sys.stdin.readline

n = int(input())    #입력: 380

coin = [500, 100, 50, 10, 5, 1]
count = 0

# 620원에 대해서 잔돈을 몇개를 줘야하는지 알아내야함
cash = 1000 - n
for i in coin:
    count += cash//i    #1. 큰잔돈(500)부터 순차적으로 진행 620//500 = 1
    cash %= i   #2. 620 % 500 = '120' ->으로 1~2다시 반복
print(count)