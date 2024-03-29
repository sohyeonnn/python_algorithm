#Backtracking
'''
# Backtracking(백트래킹)
- 현재 상태에서 가능한 모든 후보군을 따라 들어가며 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되면 즉시 후보를 포기하면서 정답을 찾아가는 범용적인 알고리즘이다.
- DFS를 기반으로하여 DFS의 비효율적인 경로를 차단하고 목표지점에 갈 수 있는 가능성이 있는 루트를 검사하는 방법
- 백트래킹은 가능성이 없는 루트를 '가지치기'로 쳐내서 탐색하는 기법이다.

- promising(유망하다: 해가 될 가능성이 있다)
=> 트리 구조를 기반으로 DFS로 깊이 탐색을 진행하면서 각 루트에 대해 조건에 부합하는지 체크한다.

- pruning(가지치기: 유망하지 않은 노드에 가지 않는것)
=> 해당 트리에서 조건에 맞지않는 노드는 더 이상 DFS로 깊이 탐색을 진행하지 않고 가지치기를 한다.

- 구현
[step1]가상의 트리에서 해를 구하기 위해 부모 노드에서 자식 노드까지 뻗어나간다.
[step2]만약 해당 노드가 조건에 맞지 않는다면 다시 부모노드로 돌아간다.

    => 해가 아닌 선택지는 없애면서 탐색하기 때문에 시간복잡도를 줄일 수 있다.
'''