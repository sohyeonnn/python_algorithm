#트리 순회_(실1)
'''
이진트리를 입력받아 전/중/후위 순회 한 결과를 출력하는 프로그램 작성

#리스트로 트리 생성해서 풀었더니
'list indices must be integers or slices, not str'오류 발생
    => 딕셔너리 형태로 바꾸니까 정상 작동
'''
import sys
n = int(sys.stdin.readline().rstrip())
tree = {}

class BinaryTree:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def preorder(node):
    print(node.data, end='')
    if node.left_node != None:
        preorder(tree[node.left_node])
    if node.right_node != None:
        preorder(tree[node.right_node])

def inorder(node):
    if node.left_node != None:
        inorder(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        inorder(tree[node.right_node])

def postorder(node):
    if node.left_node != None:
        postorder(tree[node.left_node])
    if node.right_node != None:
        postorder(tree[node.right_node])
    print(node.data, end='')


for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == ".":
        left_node = None
    if right_node == ".":
        right_node = None
    tree[data] = BinaryTree(data, left_node, right_node)


preorder(tree['A'])    #전위순회
print()
inorder(tree['A'])      #중위순회
print()
postorder(tree['A'])    #후위순회