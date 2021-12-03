#내리막 길_(골4)_dp
'''
세로: m
가로: n

항상 내리막길로만 이동하는
=> 항상 아래로만 간다는건지/ 주변 수 중 가장 작은 수로만 간다는건지?
'''
'''
import sys

m, n = map(int, sys.stdin.readline().split())
height = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[] * n for _ in range(m)]    #dp맵 생성
dp[0][0] = 1

#dx = [0, 1, 0, 0]
#dy = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):

        #now = height[i][j]

        nx = i + height[i][j]
        ny = j + height[i][j]

        if  height[i-1][j-1] > height[i][j]:
            if nx < m:
                dp[nx][j] += dp[i][j]
            if ny < n:
                dp[i][ny] += dp[i][j]

print(dp)
print(dp[-1][-1])
'''

#dfs+dp(메모이제이션)
'''
dfs + dp:
dfs로 탐색하고 dp로 배열에 각 칸마다의 결과 값을 저장해 나감.
이전에 갔었던 칸을 지나갈 시 dp에서 답을 가져와서 사용함으로서
깊이 탐색의 시간을 줄인다. 

dp[i][j]: 내리막길의 경우의 수
1. 0이면 목적지까지 갈 수 있는 경로가 없으므로 0을 반환
2. 1이상의 값이면 이전에 연산한 방문 경로가 있으므로 해당 값을 반환해서 더해준다.
3. -1이면 방문하지 않은 경로이므로 정상적으로 def실행
'''
import sys
sys.setrecursionlimit(10**9)       #런타임에러해결
m, n = map(int, sys.stdin.readline().split())
height = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]   #반복계산 방지를 위해 -1로 초기화함
#dp[m-1][n-1] = 1

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    #도착 지점일시 1반환
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] == -1:  #방문하지 않았던곳은 상하좌우를 가기 전에 -1에서 0으로 바꾼다.
        dp[x][y] = 0    #방문했으므로 방문표시(0)해준다

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                #상하좌우중에서 작은 값이 있는 경우 반환된 값을 현재의 dp로 저장한다.
                if height[x][y] > height[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    #dfs호출된게 반환되며 dp[0][0]을 반환하게 된다.
    return dp[x][y]


print(dfs(0,0))

