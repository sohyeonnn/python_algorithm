#섬의 개수(실2)_dfs, bfs
'''
가로,세로,대각선으로 연결되어있는 사각형은 걸어갈 수 있는 사각형이다.

테스트케이스 여러개가 주어진다.

w, h = 너비(가로) 높이(세로)
지도가
주
어
짐  1=땅, 0=바다
마지막 줄에는 0 0 을 입력하여 입력을 종료한다.

*point
대각선 좌표를 고려해주는것이 포인트이다!
(dx, dy에 대각선 위치를 같이 써줄것)

'''
import sys
sys.setrecursionlimit(10000)    #런타임에러(recursion error) 해결
from collections import deque
input = sys.stdin.readline


#대각선 위치를 고려한 dx, dy 이동
dx = [-1, 1, -1, 1, 0, 0, -1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

'''
#dfs풀이
def dfs(x, y):

    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:  #범위안에 해당하며 섬/땅이라면
            field[nx][ny] = -1  #방문처리하고
            dfs(nx, ny)     #해당 위치(nx, ny로 이동한 위치)에서 dfs를 다시 수행해준다
'''

#bfs풀이
def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:  # 범위안에 해당하며 섬/땅이라면
                field[nx][ny] = -1  # 방문처리하고
                queue.append([nx, ny])


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:   #0 0 이 입력되면 종료시킨다
        break

    field = []  #0과 1을 입력받을 빈 리스트 생성
    island = 0  #섬 개수 counting

    for _ in range(h):  #세로길이만큼 입력받음
        field.append(list(map(int, input().split())))   #field에 0과 1을 저장함

    for i in range(h):  #세로
        for j in range(w):  #가로
            if field[i][j] == 1:    #1이라면(섬/땅이라면)
                #dfs(i, j)   #dfs를 실행한다
                bfs(i, j)   #bfs를 실행한다.
                island += 1     #섬 개수를 1 늘려준다.

    print(island)
