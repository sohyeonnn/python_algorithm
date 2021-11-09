#바이러스(실3)_BFS
'''
-input; 컴퓨터의 수(<=100)
네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수
한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍

- 양방향 그래프라서 네트워크 정보를 한번 뒤집어서 2차원 배열에 넣어준다.

-
b = [[0] * 2 for _ in range(3)]
b[0][0] = 1

=> 출력; [[1, 0], [0, 0], [0, 0]]
'''

#BFS풀이
import sys
from collections import deque

Com = int(sys.stdin.readline().rstrip())
DirecCom = int(sys.stdin.readline().rstrip())
VirusGraph = [[0] * (Com+1) for i in range(Com+1)]

#2차원 배열 안에 넣어주기
for i in range(DirecCom):
    ComNum1, ComNum2 = map(int, sys.stdin.readline().split())
    VirusGraph[ComNum1][ComNum2] = VirusGraph[ComNum2][ComNum1] = 1


#1번째 com과 연결된 모든 노드 뽑기
def bfs(VirusGraph, start):

    queue = deque([start])
    visited = []

    ''' 수정전코드
    queue = deque()
    queue.append([start])
    visited = []
    '''

    while queue:
        now = queue.popleft()
        visited.append(now)

        for i in range(len(VirusGraph)):
            if VirusGraph[now][i] and i not in visited and i not in queue:
                queue.append(i)
    return len(visited)-1

#1com을 제외한 감염된 노드 수 출력
print(bfs(VirusGraph, 1))