#다익스트라 연장선...
#Floyd-Warshall
'''
# 플로이드-워셜 알고리즘 개요
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.
- 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행한다.
    => 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
- 2차원 테이블에 최단 거리 정보를 저장한다.
- 갈 수 없는 경로는 INF로 표시한다.
- DP유형에 속한다.
- 점화식을 사용하기 때문에 -> 3중 for문으로 동작한다.
- 시간복잡도: [ O(N**3) ]
    => 따라서 노드의 개수가 적은 상황에서 효과적으로 사용 할 수 있다.
    => 노드의 개수나 간선의 개수가 많다면 다익스트라를 사용한다.


# 플로이드-워셜 알고리즘
- 각 단계마다 특정한 노드 k를 거쳐가는 경우를 확인한다.
    => a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사한다.


#플로이드 성능 분석
- 노드의 개수가 n개 일 때 알고리즘 상으로 n번의 단계를 수행한다.
    => 각 단계마다 O(N**2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려한다.
- 시간복잡도: [ O(N**3) ]
'''


#플로이드 워셜 알고리즘
import sys

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]    #최단경로를 담는 대열

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

def floyd():

    #최단 경로를 담는 배열 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for k in range(n):  #거치는 점
        for i in range(n):  #시작점
            for j in range(n):  #끝점
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                #if graph[i][j] > graph[i][k] + graph[k][j]:
                #   graph[i][j] = graph[i][k] + graph[k][j]
    return graph

res = floyd()
for i in range(1, n+1):
    for j in range(1, n+1):
        print(res[i][j], end=' ')
    print()
