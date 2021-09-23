#분수찾기(브1)
'''
- 시간제한유의
- 1 3 6 10 15 ...(마지막 수 기준)
- 라인인덱스기준 ; 수 점점 커짐
-
'''

import sys
import time
start_time = time.time()

n = int(sys.stdin.readline().rstrip())

line = 0        #사선라인
max_index = 0   #해당 사선 라인에서의 마지막 인덱스(1, 3, 6, 10, ...)

while n > max_index:        #max_index가 입력n에 도달할 때 까지만 while문을 반복한다.
    line += 1               #사선 라인 하나씩 증가
    max_index += line       #사선라인에 있는 정수중 가장 큰 정수를 찾는데 사용된다.

    gap = max_index - n
    #해당 사선 라인에서 제일 큰 수에서 입력받은 수를뺀다.


if line % 2 == 0:       #사선 라인이 짝수 라인일 때
    top = line - gap    #분자
    under = gap + 1     #분모
else:                   #사선 라인이 홀수 라인일 때
    top = gap + 1
    under = line - gap

print(f"{top}/{under}")

end_time = time.time()
print("프로그램 수행시간: ", end_time-start_time)