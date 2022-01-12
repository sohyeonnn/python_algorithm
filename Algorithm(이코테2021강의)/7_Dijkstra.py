#Dijkstra
'''
# 다익스트라 = 최단 경로 알고리즘
: 가장 짧은 경로를 찾는 알고리즘을 말한다.

- (적용 가능한)다양한 문제 상황
    => 한 지점에서 다른 한 지점까지의 최단 경로
    => 한 지점에서 다른 모든 지점까지의 최단 경로
    => 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 노드로 표현한다.
- 지점 간 연결된 도로는 그래프에서 간선으로 표현한다.


# 다익스트라 알고리즘
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산한다.
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작한다.
    => 현실 세계의 도로(간선)은 음의 간선으로 표현할 수 없기 때문
- 다익스트라 알고리즘은 그리디 알고리즘으로 분류된다.
    => 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다.(그리디)
    **최단경로 알고리즘은 DP로 분류되기도 한다.


# 다익스트라 알고리즘 동작 과정
    [step1] 출발 노드를 설정한다.
    [step2] 최단 거리 테이블을 초기화 한다
        => 기본적으로 모든 노드까지 가기 위한 비용을 inf(무한)으로,
           자기 자신에 대한 노드는 0으로 설정한다.(나->나 로 가는 비용은 0이기 때문)
    [step3] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
    [step4] 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
    [step5] 위 과정에서 [step3]과 [step4]를 반복한다.
**다익스트라 알고리즘을 수행할 때 마지막 노드에 대한 거리값을 처리하지 않아도 값을 얻을 수 있다.


# 다익스트라 알고리즘의 특징
- 그리디 알고리즘에 속함: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다.
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다.
    => 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다.
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장된다.
    => 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 한다.


# 다익스트라 알고리즘 성능 분석
- 총 [ O(V) ] 번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다.
- 전체시간복잡도: [ O(V**2) ] => 이때 v는 노드의 개수이다.
- 일반적인 코테에서는 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 아래 간단 구현 코드로 문제를 해걸할 수 있다
    =>하지만 노드의 개수가 10000개가 넘어간다면?

----------------

#우선순위 큐(Priority Queue)
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
- 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건(우선순위가 높은)부터 꺼내서 확인해야 하는 경우에 활용 가능하다.


#힙(heap)
- 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나이다.
- 최소힙(Min Heap)과 최대힙(Max Heap)이 있다.
- 다익스트라 최단 경로 알고리즘을 포함해, 다양한 알고리즘에서 사용된다.

----------------

#다익스트라 알고리즘의 개선된 구현방법 -> 힙 이용
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용한다.
- 다익스트라 알고리즘이 동작하는 기본 원리는 동일하다.
    => 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다르다.
    => 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용해야 한다.


#힙 자료구조 이용_다익스트라 알고리즘의 성능 분석
- 시간복잡도: [ O(ElogV) ]
- 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사하다.
    => 시간복잡도를 O(ElogE) 와 같이 판단할 수 있다.
    => 중복간선을 포함하지 않는 경우 O(ElogV)로 정리할 수 있다.
'''


# 간단 구현
#단계마다 방문하지 않은 노드 중, 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인한다.
'''
import sys
input = sys.stdin.readline

INF = sys.maxsize   #테이블을 초기화 할 때 무한 값을 사용

n, m = map(int, input().split())    #노드 개수, 간선 개수 입력
start = int(input())    #시작 노드 번호 입력
graph = [[] for i in range(n+1)]    #연결리스트 형태로 그래프 초기화/ 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)   #방문체크 목적의 리스트/ 모든 노드에 대해 아직 방문이 안되었으니 false값을 넣어줌
distance = [INF] * (n+1)    #최단 거리 테이블을 모두 무한으로 초기화

#모든 간선 정보를 입력받음
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    #a번째 리스트는 b,c를 하나의 튜플로 묶어서 넣어주도록 한다.


#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
    min_value = INF
    index = 0   #가장 최단거리가 짧은 노드(인덱스)

    for i in range(1, n+1): #1~n까지 모든 노드를 하나씩 확인
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index    #방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드를 반환


#다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0     #시작 노드에 대해서 초기화/ 출발 노드까지의 거리는 0으로 갱신
    visited[start] = True   #시작노드 방문처리

    for j in graph[start]:  #출발 노드로 부터 당장 도달이 가능한 다른 노드까지의 거리를 갱신
        distance[j[0]] = j[1]

    #시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    for i in range(n-1):
        now = get_smallest_node()   #현재 거리가 가장 짧은 노드를 꺼내서, 방문처리
        visited[now] = True

        for j in graph[now]:    #그렇게 꺼내진 노드=현재 노드와 연결된 다른 노드를 하나씩 확인
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:   #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으 경우
                distance[j[0]] = cost   #해당 비용으로 테이블을 갱신

dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
'''


#최소 힙 예제
#파이썬은 최소힙 방식으로 라이브러리가 구현되어 있기 때문에 데이터를 꺼낼 때  우선순위가 낮은 데이터부터 나온다.
'''
import heapq

#오름차순 힙정렬
def heapsort(iterable):
    heap = []
    result = []

    for value in iterable:
        heapq.heappush(heap, value)

    for i in range(len(heap)):
        result.append((heapq.heappop(heap)))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
'''


#최대 힙 예제
'''
import heapq

#내림차순 힙정렬
def heapsort(iterable):
    heap = []
    result = []

    for value in iterable:
        heapq.heappush(heap, -value)    #(최소힙기준으로) 부호를 바꿔서 넣고

    for i in range(len(heap)):
        result.append((-heapq.heappop(heap)))   #부호를 바꿔서 꺼내면
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)   #최대힙 예제로 볼 수 있다.
'''


#heap을 이용한 다익스트라 구현 예제
'''
import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize   #테이블을 초기화 할 때 무한 값을 사용

n, m = map(int, input().split())    #노드 개수, 간선 개수 입력
start = int(input())    #시작 노드 번호 입력
graph = [[] for i in range(n+1)]    #연결리스트 형태로 그래프 초기화/ 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1)

#모든 간선 정보를 입력받음
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    #a번째 리스트는 b,c를 하나의 튜플로 묶어서 넣어주도록 한다.


#다익스트라 알고리즘
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))    #(힙)큐에 넣어줌/ 출발 노드의 거리가 0으로 설정
    distance[start] = 0     #출발 노드로 가기 위한 최단거리 값을 0으로 설정

    #우선순위 데이터가 0이 될 때 까지 수행
    while heap:
        dist, now = heapq.heappop(heap)     #(현재꺼낸원소의)거리, 노드/가장 최단거리가 짧은 노드에 대한 정보가 먼저 꺼내짐

        if distance[now] < dist:    #현재 노드가 이미 처리된 적 있는 노드라면 = 현재 꺼낸 원소의 거리값이 테이블에 기록되어 있는 값보다 크다면 이미 처리된것으로 간주
            continue    #무시
        for i in graph[now]:    #현재 노드와 연결된 다른 인접한 노드의 정보를 확인
            cost = dist + i[1]  #i[1]; 거리값을 의미함 / 현재 확인하고 있는 노드까지의 거리 값 + 그노드와 인접한 다른 노드의 거리값

            if cost < distance[i[0]]:   #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=' ')
'''
'''
입력예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 3
3 2 3
3 6 5
4 3 3 
4 5 1
5 3 1
5 6 2

출력: 0 2 3 1 2 4 
'''


#<문제> 전보
'''
import sys
import heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())  #노드 개수, 간선 개수 입력, 시작도시

INF = sys.maxsize   #테이블을 초기화 할 때 무한 값을 사용

graph = [[] for i in range(n+1)]    #연결리스트 형태로 그래프 초기화/ 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1)

#모든 간선 정보를 입력받음
for _ in range(m):
    a_city, b_city, cost = map(int, input().split())
    graph[a_city].append((b_city, cost)) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    #a번째 리스트는 b,c를 하나의 튜플로 묶어서 넣어주도록 한다.


#다익스트라 알고리즘
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, c))    #(힙)큐에 넣어줌/ 출발 노드의 거리가 0으로 설정
    distance[c] = 0     #출발 노드로 가기 위한 최단거리 값을 0으로 설정

    #우선순위 데이터가 0이 될 때 까지 수행
    while heap:
        dist, now = heapq.heappop(heap)     #(현재꺼낸원소의)거리, 노드/가장 최단거리가 짧은 노드에 대한 정보가 먼저 꺼내짐

        if distance[now] < dist:    #현재 노드가 이미 처리된 적 있는 노드라면 = 현재 꺼낸 원소의 거리값이 테이블에 기록되어 있는 값보다 크다면 이미 처리된것으로 간주
            continue    #무시
        for i in graph[now]:    #현재 노드와 연결된 다른 인접한 노드의 정보를 확인
            city_cost = dist + i[1]  #i[1]; 거리값을 의미함 / 현재 확인하고 있는 노드까지의 거리 값 + 그노드와 인접한 다른 노드의 거리값

            if city_cost < distance[i[0]]:   #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = city_cost
                heapq.heappush(heap, (city_cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0

#모든 도시가 메세지를 받는데 걸리는 시간
for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance, i)

print(count-1, max_distance)
'''


#미래도시
import sys

INF = sys.maxsize

n, m = map(int, input())

graph = [[INF] * n for _ in range(n)]    #최단경로를 담는 대열

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1  #양방향 그래프

x, k = map(int, input())

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

distance = floyd()
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)