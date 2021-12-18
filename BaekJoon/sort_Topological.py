#위상 정렬(Topological Sort)
'''
- 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 순서를 결정할 때 사용하는 알고리즘.
- 방향 그래프에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서 모든 정점을 나열하면 된다.
- 하나의 방향 그래프에는 여러 개의 위상 정렬이 가능하다.
    => 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는것을 의미한다.


*진입차수와 진출차수(indegree & outdegree)
- 진입차수: 특정한 노드로 들어오는 간선의 개수
- 진출차수: 특정한 노드에서 나가는 간선의 개수


*위상 정렬 알고리즘
: 큐(queue)를 이용
    [step1] 진입차수가 0인 (모든)노드를 queue에 넣는다.
    [step2] -1) queue에서 하나의 정점을 선택하여
            -2) 선택한 정점을 queue에서 삭제하고 위상순서에 추가한다.
    [step3] 선택한 정점에 연결된 간선을 모두 삭제한다.
    [step4] 1 ~ 3을 반복한다.
=> 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.


*위상 정렬 알고리즘 시간 복잡도
- 위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거해야한다.
- 시간복잡도: O( V + E)
'''

import sys
from collections import deque

#노드, 간선 개수 입력 받음
v, e = map(int, sys.stdin.readline().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

#각 노드에 연결된 간선의 정보를 담기 위한 연결리스트 초기화
graph = [[] for _ in range(v+1)]

#방향 그래프의 간선 정보를 입력받음
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)      #정점A에서 B로 이동

    indegree[b] += 1    #진입차수를 1 증가


#위상정렬 함수
def TopologicalSort():
    queue = deque()
    topology = []       #알고리즘 수행 결과를 담을 리스트
    global indegree     #참조 문제 때문에 global

    #처음 시작할 때 진행 차수가 0인 노드를 큐에 삽입한다.
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)


    while queue:
        #큐에서 원소를 꺼냄
        now = queue.popleft()
        topology.append(now)

        #해당 원소와 연결된 노드들의 진입차수에서 1을 뺀다.
        for i in graph[now]:
            indegree[i] -= 1

            #새롭게 진입차수가 0이되는 노드를 큐에 삽입한다.
            if indegree[i] == 0:
                queue.append(i)
    # 큐가 빌때까지 반복한다.

    #위상 정렬을 수행한 결과를 출력한다.
    for i in topology:
        print(i, end=' ')

TopologicalSort()