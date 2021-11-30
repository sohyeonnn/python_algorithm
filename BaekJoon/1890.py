#점프_(실2)
'''
sol1>>
bfs문제같은데...?
-> 메모리초과

sol2>>
dp
'''

'''
#bfs풀이
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

jump_box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#print(jump_box)
queue = deque()
queue.append([0, 0])


#우측이나 아래로만 움직일 수 있음
dx = [0, 1, 0, 0]
dy = [0, 0, 0, 1]

ans = 0

while queue:
    x, y = queue.popleft()      
    weight = jump_box[x][y]

    for i in range(4):      
        if jump_box[x][y] == 0:
            continue

        nx = dx[i]*weight + x
        ny = dy[i]*weight + y

        if nx == n-1 and ny == n-1:
            ans += 1
            continue

        if 0 <= nx < n and 0 <= ny < n:
            if jump_box[nx][ny] != 0:
                queue.append([nx, ny])

print(ans)
'''

#dp풀이

import sys

n = int(sys.stdin.readline().rstrip())
jump_box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]    #dp맵
dp[0][0] = 1    #dp맵 시작지점만 1로 초기화해줌

#우측이나 아래로만 움직일 수 있음
dx = [0, 1, 0, 0]
dy = [0, 0, 0, 1]


for i in range(n):
    for j in range(n):
        now = jump_box[i][j]

        nx = i + now
        ny = j + now

        if now > 0:
            if nx < n:
                dp[nx][j] += dp[i][j]
            if ny < n:
                dp[i][ny] += dp[i][j]

#print(dp)      도착지점(우측아래)에 도달 가능한 경우의수가 쌓여있음
print(dp[-1][-1])