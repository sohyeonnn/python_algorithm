#중량제한(골4)
'''
각각의 다리마다 중량제한이 있다,
중량제한을 초과하는 양의 물품이 다리를 지나게 되면, 다리가 무너지게 된다.
모든 다리는 양방향이다

한 번의 이동으로 옮길 수 있는 중량의 최댓값을 구하는 알고리즘을 작성

**point
그래프 내의 간선이 많은 경우 프림이 유리하다는 것을 기억할 것

- 풀이방법:
최소스패닝트리 변형 방법으로 풀었음
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

road = []
for _ in range(m):
    a, b, c = map(int, input().split())
    road.append((c, a, b))
road.sort(reverse=True)
#=> 최대한 무거운 물건을 옮기기 위해 최소가 아닌 최대 스패닝 트리를 구한다

fac1, fac2 = map(int, input().split())

#부모 테이블 상에서 부모를 자기 자신으로 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY


#fac1과 fac2가 연결된 집합에 속하는 순간 얻고자 하는 경로가 완성되기 때문에 break하고 출력해준다.
for i in road:
    c, x, y = i[0], i[1], i[2]
    #간선을 선택해서
    union(parent, x, y)
    # union함수는 두 원소가 속한 집합을 합치는 연산 (=간선 연결한다고 생각!)
    if find(parent, fac1) == find(parent, fac2): #만약 간선이 연결된다면 원하는 답을 얻은 것이므로
        break
print(c)