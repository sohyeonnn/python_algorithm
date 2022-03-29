#보류
#DFS와 BFS(실2)
'''
n: 정점의 개수
m: 간선의 개수(양방향)
v: 탐색을 시작할 정점의 번호

[DFS] => 재귀 부분과 초기화, 실행 부분을 따로 만들어주는 것이 중요
1. stack에 시작 노드를 넣는다.
2. stack이 비어있으면 실행을 멈추고 False 반환
3. stack의 맨 위 노드가 찾고자 하는 노드라면 탐색을 종료하고 True 반환
4. 3번에서 stack의 맨 위 노드가 찾고자하는 노드가 아니라면 해당 노드를 pop하고,
    stack에 들어온 적 없는 pop한 노드의 모든 이웃 노드를 찾아 순서대로 stack에 push
5. 3으로 돌아간다


*review1>
1. graph = [[0] * (n+1) for i in range(n+1)]
=> 메모리초과
2. graph = [[] * (n+1) for i in range(n+1)]
=> 런타임 에러
해결!3. 양방향 간선 처리를 바꿈
graph[m1].append(m2)
graph[m2].append(m1)

**review2> 예제2부터 출력오류발생(11%)
해결1. bfs부터 방문처리 queue에 넣을때 sorted해줌
해결2. dfs는 reversed(sorted())해서 처리
'''

'''
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[]*(n+1) for i in range(n+1)]

#간선이 연결하는 두 정점의 번호
for i in range(m):
    m1, m2 = map(int, sys.stdin.readline().split())
    #양방향 간선
    graph[m1].append(m2)
    graph[m2].append(m1)
    #graph[m1][m2] = graph[m2][m1] = 1


def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        now = stack.pop()
        #visited[now] = True
        if now not in visited:
            visited.append(now)
            stack += reversed(sorted(graph[now]))
    return visited


def bfs(graph, v):
    visited = []
    queue = deque([v])

    while queue:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            queue += sorted(graph[now])
    return visited


print(' '.join(list(map(str, dfs(graph, v)))))
print(' '.join(list(map(str, bfs(graph, v)))))
'''

'''
def bfs(graph, startV):

    queue = deque([startV])
    visited = []
    #visited[startV] = True

    while queue:
        now = queue.popleft()
        #print(now, end = ' ')
        #visited.append(now)

        if now not in visited:
            visited.append(now)
            #queue.append(i)
            #visited[i] = True
            queue += graph[n]
    return visited


print(bfs(graph, startV))
'''

import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())    #정점개수/간선개수/시작정점번호
graph = [[] for i in range(n+1)]


for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)    #인접리스트로 구현

#print(graph)    # [[], [2, 3, 4], [1, 3], [1, 2, 4], [1, 3]]


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    graph[start].sort()     #**문제조건; 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은것을 먼저 방문
    for node in graph[start]:

        if not visited[node]:
            dfs(graph, node, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        graph[now].sort()       #**문제조건; 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은것을 먼저 방문
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n+1)

dfs(graph, start, visited)
visited = [False] * (n+1)
print()
bfs(graph, start, visited)