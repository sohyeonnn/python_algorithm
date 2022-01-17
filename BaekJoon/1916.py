#최소비용 구하기(골5)
'''
a -> b 로 가는 비용을 최소화
=> 플로이드?
=> 다른 도시를 거쳐 가더라도 출발-도착에 걸리는 최소 비용을 알아내면 됨

**sol
다익스트라 이용
- 왜?
: 특정점->특정점 으로의 최단거리이기때문에 다익스트라!

'''

import heapq, sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())    #도시개수
m = int(input())    #버스개수(간선)

distance = [INF] * (n+1)    #도착지까지 가는 최단경로 테이블

graph = [[] for _ in range(n+1)]
for _ in range(m):  #버스의 이동정보
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())


def dijkstra(s):
    h = []
    heapq.heappush(h, (0, s))   #힙큐에 출발점을 넣어줌(거리, 출발지점)
    distance[s] = 0

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
dijkstra(s)

print(distance[e])