#퇴사(실3)
'''
*백준_회의실문제랑 비슷?

*재귀함수

바텀업방식, 작은 문제부터 확인해서 최종 결과값을 도출한다
뒤애서부터 확인해서 DP값을 갱신한다

*아래 두 값을 비교해서 더 큰값으로 갱신한다.
    case1. i번째 일을 할 떄의 이익; cost[i] + dp[i + time[i]]
    case2. i번째 일을 건너뛰고 i+1번째 일을 할 때의 이익; dp[i+1]

* 문제에서 dp 메인 점화식
dp[i] = max(dp[i+1], cost[i] + dp[i + time[i]])
'''


import sys

n = int(sys.stdin.readline().rstrip())

time = []
cost = []
dp = []

for i in range(n):
    Ti, Pi = map(int, sys.stdin.readline().split())
    time.append(Ti)
    cost.append(Pi)
    dp.append(Pi)
dp.append(0)    #error방지; index list out of range

for i in range(n-1, -1, -1):    #뒤에서부터 확인
    if time[i] + i > n:     #데드라인이 기한을 넘어가는 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], cost[i] + dp[i + time[i]])
print(dp[0])
