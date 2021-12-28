#선수과목(prerequisite)
'''
#위상정렬문제

선수과목 듣는데 걸리는 학기 수 == 해당 노드로 이동하는 수

- 풀이 방법
: 위상정렬의 경우, indegree(나에게 들어오는 edge수)가 0이 될 때마다 '나'를 수행하면 된다.

1) 입력으로 받은 값들로 indegree를 설정해주고
2) 처음이 0인 node부터 탐색하고
3) 0이 될 때 마다 해당 node를 수행하면

'''
import sys
from collections import deque

#첫 줄
n, m = map(int, sys.stdin.readline().split())

#각 노드에 연결된 간선의 정보를 담기 위한 연결리스트 초기화
graph = [[] for _ in range(n+1)]

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)
ans = [0] * (n+1)

#방향 그래프의 간선 정보를 입력받음
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # 정점A에서 B로 이동
    indegree[b] += 1  # 진입차수를 1 증가


#위상정렬 함수
def TopologicalSort():
    queue = deque()

    #처음 시작할 때(시작점을 잡기 위해) 진행 차수(indegree)가 0인 노드를 큐에 삽입한다.
    for i in range(1, n+1):     #0번째 인덱스 띄워주기위해 1 ~ n+1로 range설정
        if indegree[i] == 0:
            queue.append(i)
            ans[i] = 1      #원래 0인 곳에는 1을 넣어줌


    while queue:
        #큐에서 원소를 꺼냄
        now = queue.popleft()

        #해당 원소와 연결된 노드들의 진입차수에서 1을 뺀다.
        for i in graph[now]:
            indegree[i] -= 1    #탐색한 지점의 indegree를 1씩 감소시킨다.
            ans[i] = ans[now] + 1

            #감소시켯을 때 새롭게 진입차수(indegree)가 0이되는 노드를 큐에 삽입한다.
            if indegree[i] == 0:
                queue.append(i)
    # 큐가 빌때까지 반복한다.

    #위상 정렬을 수행한 결과를 출력한다.

TopologicalSort()

print(*ans[1:])
'''
- *를 사용해서 객체의 압출을 풀고 대괄호 없이 출력
- index 0번째는 0번째 이기 때문에 [1:] 로 index 1뒤의 모든 원소를 출력해준다.
'''