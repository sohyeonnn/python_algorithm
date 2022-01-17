#최단경로
'''
- 최소힙으로구현
'''

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())    #start; 시작정점의 번호

distance = [INF] * (v+1)

graph = [[] for _ in range(v+1)]    #연결 된 노드의 정보를 담기위해 연결리스트 형태의 그래프를 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     #a출발노드, b도착노드, c가중치
#print(graph)

def dijkstra(k):
    h = []
    heapq.heappush(h, (0, k))   #힙큐에 출발점을 넣어줌(거리, 출발지점)
    distance[k] = 0

    while h:
        dist, now = heapq.heappop(h)    #거리값, 현재꺼낸노드에 대한 정보

        if distance[now] < dist:    #현재 꺼낸 원소의 거리값(dist)이 테이블에 있는 값보다 크다면,
            continue    #현재 꺼낸 노드가 이미 처리된 적 있는(것으로 간주하여) 노드라면 무시

        #현재 노드와 연결된 다른 인접노드들의 정보를 확인
        #print(graph[now])

        for to, weight in graph[now]:   #현재 노드에서 가고자 하는 노드, 비용
            cost = dist + weight    #가고자 하는 노드 까지의 비용
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(h, (cost, to))   #힙큐에 도착 노드와 비용을 push

        '''
        for i in graph[now]:
            cost = dist + i[1]      #dist; 현재 확인하고 있는 노드까지의 거리값/i[1]는 (현재노드와 연결된)거리값을 의미한다.
            #cost = 현재 확인하고 있는 노드까지의 거리값 + 그 노드와 인접한 다른노드의 거리값

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
        '''

dijkstra(k)


for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])