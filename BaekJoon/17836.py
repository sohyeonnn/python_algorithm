#공주님을 구해라!
'''
최단거리... -> bfs!

#17퍼 런타임에러 때문에 엄청 헤멧다
-> 공주한테 갈 수 있는 경우는 출력이 되는데 Fail을 못찾음

*해결*
전: visited = [[0] * n for _ in range(n)]
후: visited = [[0] * m for _ in range(n)]
-> visited배열을 n*n으로 놓음... 고쳐주니 바로 통과함.
'''

import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())

castle = []
for i in range(n):
    castle.append(list(map(int, sys.stdin.readline().split())))
visited = [[0] * m for _ in range(n)]

#용사는 상하좌우로 이동할 수 있다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    #global princess
    princess = 987654321
    queue = deque([])
    queue.append((0,0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if castle[x][y] == 2:   #검을만나면
            #검을만난 위치에서 공주가 있는 (n-1, m-1)과의 좌표 차이값을 더해준다
            princess = abs(n-1-x) + abs(m-1-y) + visited[x][y] -1
        #공주가 있는 곳에 도착하면
        if x == n-1 and y == m-1:
            #현재 시간과 pricess의 최솟ㄷ값을 저장하도록 한다.
            return min(visited[x][y]-1, princess)

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if castle[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return princess

res = bfs()
if res > t:
    print("Fail")
else:
    print(res)