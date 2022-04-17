#벽 부수고 이동하기(골4)_bfs
'''
0; 이동할 수 있는 곳
1; 이동할 수 없는 벽
(1,1) -> (n,m)으로 이동하려 한다 '최단 경로'로
시작과 끝나는 칸도 포함해서 센다
***이동하는 도중 벽을 부수고 이동하는 것이 좀 더 빠르다면 *최대한번* 벽을 부수고이동할 수 있다

*point1
문제에 '최단경로' 라는 언급 -> bfs
'행렬로 표현되는 맵'
-> 그래프 카테고리에서 최단경로를 찾는 문제이다

*point2
기본 bfs에서 '벽을 부순다' 라는 조건이 붙은 문제

*풀이힌트
3차원 배열
visited = [[0]*2 for _ in range(m) for _ in range(n)]
-> [0]*2 인 이유는?
visited배열을 출력해 보면,  [[[0, 0], [0, 0] .. 과 같은 모양을 띄는 것을 알. 수 있는데, [0,0]인 이유는  0,1로 벽을 부수고 안부수고를 표현해주기 위함이다.
#youtube-류호석 벽 부수고 이동하기 문제 참고할것


1. 이전에 벽을 부수지 않은 경우와
이전에 벽을 부수지 않고 방문한 적이 없는 경우
- 벽인 경우
벽을 부수고 거리 +1, 방문처리
- 벽이 아닌 경우
거리 +1 , 방문처리

2. 벽을 부순 경우
이전에 벽을 부순 적이 있고 방문한 적이 없는 경우
- 벽이 아닌 경우
거리 +1, 방문처리
'''
#일반 미로탐색 문제라고 생각하고 코드 짜보기 -> 현재 코드는 미로탐색 코드임 벽부수는거로 수정해보기
#3차원 배열 사용

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())    #세로, 가로

field = []
for _ in range(n):
    field.append(list(map(int, input().rstrip())))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1    #아직 벽을 뚫은 적 없으니까 벽을 뚫을 기회가 1번 있음

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])

    while queue:
        a, b, c = queue.popleft()

        if a == n - 1 and b == m - 1:  # 우측하단(도착지점)에 도착한 경우 값을 return하고 종료한다.
            return visited[a][b][c]

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < n and 0 <= ny < m:     #범위안에 속하면서

                if field[nx][ny] == 1 and c == 0:   #벽이고 벽부술 기회를 사용하지 않은 경우
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append([nx, ny, 1])   #이번에 벽을 부순다.(c자리에 1 append = 1번 벽을 부쉇다는 의미)

                elif field[nx][ny] == 0 and visited[nx][ny][c] == 0:    #벽이 아니고 처음 와보는 곳이라면?
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append([nx, ny, c])

    else:   #도착지점에 아예 도달하지 못하는 경우에는 -1을 출력한다.
        return -1

print(bfs(0, 0, 0))

'''
wall = []
for i in range(n):
    wall.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#3차원 배열 개념 사용해야함
visited = [[[0] *2 for _ in range(m)] for i in range(n)]
visited[0][0][1] = 1    #[x][y][z]에서 z가 0이라면 벽을 한번뚫은 상태이고 1이라면 아직 벽을 뚫을 수 있는상태를 나타낸다.

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])

    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if wall[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append([nx, ny, 1])  # 방문처리
                elif wall[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])  # 방문처리
    if x == n-1 and y == m-1:   #x, y가 (n,m)위치에 도달한 경우 해당 값을 return
        return visited[x][y][z] + 1
    else:   #도달하지못하면 -1을 return
        return -1
    #return visited[x][y][z]

print(bfs(0, 0, 0))

'''
'''
#벽인데 visited가 True로 바껴있는 경우(벽인데 방문처리가 됐음-> 벽을 통과한 적이 있는 경우)
#현재 위치가 벽인데 visited가 Fasle인 경우(벽인데 방문처리 안됨->뚫을 수 있음)
                
               #이전에 벽을 부수지 않고 방문한 적이 있는 경우/없는 경우를 고려해줘야함
                if wall[nx][ny] == 1:   #벽인경우
                    wall[nx][ny] = 0    #벽을 부수고
                    wall[nx][ny] = wall[x][y] + 1   #거리 +1 해주고
                    queue.append([nx, ny])  #방문처리

                elif wall[nx][ny] == 0: #이동할 수 있는 공간인 경우우
                    wall[nx][ny] = wall[x][y] + 1   #거리 +1 해주고
                    queue.append([nx, ny])  #반문처리
'''