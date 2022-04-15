#유기농 배추(실2)_dfs
'''
0; 배추없음
1; 배추있음

배추들이 몇 군데에 퍼져있는지 조사하면 총 몇마리의 지렁이가 필요한지 알 수 있다.
-> 얼음얼리는 문제 유형
-> connected component(dfs)

1. graph=[]를 만들고 배추의 위치를 좌표로 입력받음
배추있음이니까 1롤 입력받고 없는곳은 0으로 입력받음
'''
import sys
sys.setrecursionlimit(10**7)    #재귀호출 최대 횟수를 늘려준다, 파이썬에서 기본 재귀깊이는 1000이기 때문에 이것을 늘려준것
from collections import deque
input = sys.stdin.readline

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

'''
#dfs 풀이
def dfs(x, y):

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and baechubat[nx][ny] == 1:  #범위에 속하면서 배추가 있느 경우
            baechubat[nx][ny] = -1  #방문처리
            dfs(nx, ny)
'''

#bfs 풀이
def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and baechubat[nx][ny] == 1:
                baechubat[nx][ny] = -1
                queue.append([nx, ny])


T = int(input().rstrip())   #테스트케이스 수

for _ in range(T):  #T만큼 반복
    m, n, k = map(int, input().split()) #가로, 세로, 배추 수
    baechubat = [[0]*m for _ in range(n)]
    count = 0  #지렁이... ->변수선언 위치 이유; 테케마다 각각 세고 출력해줘야 해서

    for _ in range(k):
        a, b = map(int, input().split())
        baechubat[b][a] = 1     #가로 세로 기준이니까 좌표는 반대로 넣어줘야함

    for i in range(n):
        for j in range(m):
            if baechubat[i][j] == 1:
                #dfs(i, j)
                bfs(i, j)
                count += 1

    print(count)