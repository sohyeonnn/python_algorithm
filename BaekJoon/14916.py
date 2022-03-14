#거스름돈(실5)_그리디

import sys
n = int(sys.stdin.readline().rstrip())        #n = 3인 경우 (-1이 출력되야 하는 경우)

cnt = 0
while True:
    if n % 5 == 0:  #1. (n % 5)한 값이 0이 아니기 때문에 else 문으로 이동     4. (1%5) 도 마찬가지로 0 이 아니기 때문에 else로 돌아감
        cnt += (n // 5)
        print(cnt)
        break
    else:
        n -= 2      #2. 3-2 = 1     #5. 1-2 = -1
        cnt += 1    #3. cnt에 1을 더해줌 ----> **break문이 없기 때문에 다시 선행 조건으로 돌아감   #6. cnt에 1 더해줌

    #print("n:", n)
    #print(cnt)
    if n < 0:   #7.n이 n<0의 조건을 만족하기 때문에 해당 if문으로 넘어올 수 있음(이전까지의 연산에서는 n<0의 조건을 만족하지 않았기 때문에 이 if문에 도달하지 않음)
        print(-1)     #8. if 조건을 만족함으로 -1 출력
        break   #탈출