#효율적인 해킹(실1)_DFS/BFS
#시간초과/메모리초과
#pypy3로 제출하면 통과
'''

-풀이-
신뢰하는 관계(A->B); 단방향 간선으로 생각해서 그래프 탐색
    : BFS로 탐색하면서 방문한 정점의 수를 기록한다.
최대치; 최대치를 찾아야 하므로 모든 경우를 탐색한다.
    : 최다 정점을 방문한 시작 정점의 번호를 정답으로 출력한다.
'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

#신뢰하는 관계 그래프 생성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)  # 컴퓨터 번호의 인덱스에 연결된 컴퓨터 번호를 리스트로 저장

result = []
max_value = 0

def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)  # 이미 이전에 방문한 노드인지 확인
    visited[start] = True
    count = 1

    while queue:
        now = queue.popleft()  # 큐의 앞에서부터 노드를 꺼내서

        for e in graph[now]:  # 해당 노드와 연결된 노드를 순서대로 확인
            if not visited[e]:  # 연결된 노드를 아직 방문하지 않은 경우
                queue.append(e)  # 큐에 추가 후
                visited[e] = True  # 방문한 것으로 처리
                count += 1  # 방문한 노드 수 + 1

    return count  # 주어진 노드와 연결된 노드 개수 반환


for i in range(n):  # 모든 컴퓨터 번호 확인
    count = bfs(i)  # 연결된 컴퓨터 수 확인
    if count > max_value:  # 현재 연결된 컴퓨터 수가 기존 최대 연결 컴퓨터 수보다 큰 경우
        max_value = count  # 현재 연결된 컴퓨터 수로 최대값 수정
        result = [i]  # 해당 컴퓨터 번호도 수정
    elif count == max_value:  # 현재 연결된 컴퓨터 수가 기존 최대 연결 컴퓨터 수와 같은 경우
        result.append(i)  # 해당 컴퓨터 번호 추가

for r in result:
    print(r, end=" ")

'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1   #양방향 간선 처리


def bfs(graph, start):

    queue = deque([start])
    visited = []
    cnt = 1

    while queue:
        now = queue.popleft()
        # visited.append(now)
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt
    '''
'''
        for i in range(len(graph)):
            if graph[now][i] and i not in visited and i not in queue:
                queue.append(i)
    return visited
'''
'''
#1com을 제외한 감염된 노드 수 출력
print(bfs(graph, 1))
'''