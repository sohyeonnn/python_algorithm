#트리(Tree)
'''
#트리
- 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조
- 뿌리에서부터 가지를 치면서 뻣어나가는 형태

#트리 관련 용어
- 루트 노드(root node): 부모가 없는 최상위 노드
- 단말 노드(leaf node): 자식이 없는 노드
- 크기(size): 트리에 포함된 모든 노드의 개수
- 깊이(depth): 루트 노드부터의 거리
- 높이(height): 깊이 중 최댓값
- 차수(degree): 각 노드의(자식방향) 간선 개수
=> 트리의 크기가 N일때, 전체 간선의 개수는 N-1이다.


#이진 탐색 트리(Binary Search Tree)
- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종이다.

- 이진 탐색 트리 특징;
왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드        순의 값을 가진다.
=> 부모 노드보다 왼쪽 자식 노드가 작다.
=> 부모 노드보다 오른쪽 자식 노드가 크다.

- 이진 탐색 트리에서 데이터 조회하기;
=> 찾고자 하는 값이 '37' 인 경우
[step1] 루트 노드부터 방문하여 탐색을 진행한다.      => 현재 노드와 찾는 원소 '37'을 비교 / 찾는 원소가 더 크다면 오른쪽을 방문한다.
[step2] 현재 노드와 값을 비교한다.                 => equals / 찾는 원소가 더 작으므로 왼쪽을 방문한다.
[step3] 현재 노드와 값을 비교한다.                 => equals / 원소를 찾았으므로 탐색을 종료한다.
    => 이처럼 이상적인 tree의 경우 [ O(logN) ]의 시간복잡도가 소요된다.


#트리의 순회(Tree Traversal)
- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미한다.
    => 트리의 정보를 시각적으로 확인할 수 있다.

- 트리 순회 방법;
1) 전위 순회(pre-order traverse): 루트를 먼저 방문
2) 중위 순회(mid-order traverse): 왼쪽 자식을 방문한 뒤에 루트를 방문
3) 후위 순회(post-order traverse): 오른쪽 자식을 방문한 뒤에 루트를 방문

ex)트리순회; 트리의 형태가 아래와 같을 때 각각 순회 형태
       A
    B    C
  D  E  F  G
1) 전위 순회: A-B-C-D-E-F-G
2) 중위 순회: D-B-E-A-F-C-G
3) 후위 순회: D-E-B-F-G-C-A
'''


#트리의 순회(tree traversal) 구현 예제
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')   #자신의 데이터를 먼저 처리한 뒤에
    if node.left_node != None:  #왼쪽노드
        pre_order(tree[node.left_node])
    if node.right_node != None: #오른쪽노드를 방문
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:  #왼쪽을 먼저 방문
        in_order(tree[node.left_node])
    print(node.data, end=' ')   #자기 자신을 처리
    if node.right_node != None: #오른쪽 방문
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:  #왼쪽
        post_order(tree[node.left_node])
    if node.right_node != None: #오른쪽을 방문한 뒤
        post_order(tree[node.right_node])
    print(node.data, end=' ')   #자기 자신을 처리

#트리의 크기 = 노드의 개수
n = int(input())
#전체 트리는 dictionary를 이용하여 구현
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])    #전위순회
print()
in_order(tree['A'])     #중위순회
print()
post_order(tree['A'])    #후위순회

'''
>>input;
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None

>>output;
A B D E C F G 
D B E A F C G 
D E B F G C A 
'''