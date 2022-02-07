#네트워크 연결(골4)
'''
모든 컴퓨터를 연결하는데 필요한 최소 비용을 알아내는 문제
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

network = []
for _ in range(m):
    a, b, c = map(int, input().split())
    network.append((c, a, b))
network.sort()

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


result = 0
for line in network:
    c, x, y = line

    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += c
print(result)