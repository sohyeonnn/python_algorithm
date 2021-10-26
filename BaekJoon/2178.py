#미로탐색(실1)_
'''
1 = 이동가능칸
0 = 이동불가능
- (1,1)출발 -> (n,m)이동하는 최소의 칸 수
- 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

miro = []
for i in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

    return miro[n-1][m-1]
print(bfs(0, 0))