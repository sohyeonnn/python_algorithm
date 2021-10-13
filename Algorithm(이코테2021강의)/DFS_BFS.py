#DFS/BFS
'''
#탐색(search);
- 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.


#스택(stack) 자료구조
- FILO ; ex.박스쌓기
- list로 간편하게 구현 가능(삽입: append, 삭제: pop)
- 시간복잡도; O(1)


#큐(queue) 자료구조
- FIFO ; ex. 입구랑 출구가 모두 뚫려있는 터널
- from collections import deque(삽입: append, 삭제: popleft)
- 시간복잡도; O(1)


#재귀함수(recursive function)
- 자기 자신을 다시 호출하는 함수
- python 에서는 '최대 재귀 깊이 제한'이 있기 때문에 별다른 설정이 없다면 오류메세지와함께 종료되게 된다.
- 일반적인 문제풀이 경우(일부러 무한루프를 만들지 않는 경우)에는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
- 컴퓨터가 함수를 재귀적으로 호출하게 되면, 컴퓨터 메모리 내부의 스택 프레임에 쌓이게 된다.
=> 이러한 특징때문에 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 있다.
(ex. 단순히 더 짧고 간결하게 작성하기위해(dfs))



#DFS(Depth First Search)
- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- 스택 자료구조(or 재귀함수)를 이용한다.
=>  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면, 그 노드를 스택에 넣고 방문 처리를 한다.
       방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
       **즉, 매번 최상단 노드를 기준으로 방문하지 않은 인접노드가 있으면 그 인접한 노드로도 방문을 수행하는 것.
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

- 그래프 문제가 출제되면 노드의 번호가 1번부터 시작하는 경우가 많기 때문에 list의 0번 index는 비우고 index 1부터 시작하도록 한다.


#BFS(Breadth First Search)
- 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
- 큐 자료구조를 이용한다.
=>  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
       **해당 시점에서 인접한 노드를 '한번에' 모두 큐에 넣는다는 것이 특징이다.
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

'''



#재귀함수-팩토리얼 구현 예제(**참고; 수학적으로 0!과 1!의 값은 1이다.)
'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복구현: ', factorial_iterative(5))
print('재귀구현: ', factorial_recursive(5))
'''


#재귀함수 - 유클리드 호제법 예제
'''
def gcd(a,b):
    if a%b==0:      #a가 b의 배수라면
        return b    #b를 반환
    else:
        return gcd(b, a%b)      #b와 a를 b로 나눈 나머지의 최대공약수를 반환할 수 있도록 한다.

print(gcd(192, 162))
'''


#DFS 소스코드 예제
'''
def dfs(graph, v, visit):
    visit[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#기본적으로 모든값들을 False값으로 초기화해서 처음에는 모든 노드를 방문하지 않은 것 처럼 처리할 수 있다.
#index 0을 사용하지 않게 하기위해 9를 곱함
visit = [False] * 9

dfs(graph, 1, visit)
'''


#BFS 소스코드 예제
'''
from collections import deque

def bfs(graph, start, visited):

    #시작 노드를 queue에 넣어줌.
    queue = deque([start])

    #시작 노드를 방문처리한다.
    visited[start] = True

    #이후에 큐가 빌때까지 = 더이상 수행할 수 없을 때 까지 반복한다.
    while queue:

        v = queue.popleft()         #큐에서 원소를 하나 꺼낸다.
        print(v, end=' ')

        for i in graph[v]:          #꺼낸 노드와 인접한 노드를 하나씩 확인
            if not visited[i]:      #아직 방문하지 않은게 있다면
                queue.append(i)     #큐에 다 넣어주도록 한다.
                visited[i] = True


#각 노드가 연결된 정보를 표현(그래프를 표현한 부분)
graph = [
    [],         #0번 노드에 대한 부분은 비워준다.(사용x)
    [2,3,8],    #1번 노드가 인접해있는 노드들
    [1,7],      #2번 노드가 ...
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

#방문처리 목적으로 visited 리스트를 만들어줌
visited = [False]*9

bfs(graph, 1, visited)
'''


#음료수 얼려 먹기_(DFS)/(connected component)
'''
*DFS 풀이
    1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서
    아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
    2. 방문한 지점에서 다시 상,..,우를 살펴보면서 방문을 진행하는 과정을 반복하면,
    연결된 모든 지점을 방문할 수 있다.
    3. 모든 노드에 대해 1~2의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트한다.

**문제point
; 0끼리 맞닿아 있는 곳이 하나의 얼음 덩어리, 1부분에는 음료가 안들어감

import sys

n, m = map(int, sys.stdin.readline().split())

icebox = []
for i in range(n):
    icebox.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):

    #행렬의 범위를 벗어나는 경우의 종료조건
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 탐색하는 행렬의 성분이 0인 경우(얼음이 얼수 있는 범위인 경우)
    #범위를 벗어나지 않는 경우, 현재 위치를 아직 방문하지 않았다면
    if icebox[x][y] == 0:

        #해당 부분 방문 처리한다.
        icebox[x][y] = 1

        #재귀호출
        dfs(x - 1, y)       #상
        dfs(x + 1, y)       #하
        dfs(x, y - 1)       #좌
        dfs(x, y + 1)       #우
        return True
    return False        #0이 아닌 부분에서는 False를 반환하게 함


count = 0

#n*m크기
for i in range(n):
    for j in range(m):

        #현재 위치에서 DFS 수행하여 방문처리가 된거라면, count를 진행
        if dfs(i,j) == True:
            count += 1
print(count)
'''


#미로 탈출
'''
(1,1)을 이미 방문한상태로 문제를 해결해야 하기 때문에 -> bfs?

*BFS 풀이
    1. BFS; 간선의 비용이 모두 같을 때 최단 거리를 탐색하기 위해 사용하는 알고리즘
    => 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
    2. 상하좌우로 연결된 모든 노드로의 거리가 1로 동일하다.
    => (1,1)의 지점부터 BFS를 수행하여 모든 노드의 최단거리값을 기록하면 해결할 수 있다!
    

'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

#2차원 리스트의 맵 정보 입력 받기
miro = []
for i in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))


#이동할 네 가지 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):

    queue = deque()
    queue.append((x, y))        #x,y로 이루어진 tuple 데이터를 담는다.

    while queue:
        x, y = queue.popleft()      #반복할 때마다 큐에서 한가지 원소를 꺼낸다.

        #반복할 때마다 현재 위치에서 4가지 방향으로 위치를 확인한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #연결된 위치가 미로 공간을 벗어난다면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            #이동할 수 없는 위치인 경우에도 무시
            if miro[nx][ny] == 0:
                continue

            #해당 노드를 처음 방문하는 경우에만 최단거리를 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1       #바로 직전 노드에서의 최단거리값에 +1 해준다.
                queue.append((nx, ny))      #queue에 데이터를 넣으면서 거리값을 증가시킬 수 있다.

    #가장 오른쪽 아래까지의 최단 거리를 반환한다.
    return miro[n-1][m-1]

print(bfs(0, 0))