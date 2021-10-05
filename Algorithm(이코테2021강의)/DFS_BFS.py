#DFS/BFS
'''
#탐색(search);
- 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.


#스택(stack) 자료구조
- FILO ; ex.박스쌓기
- list로 간편하게 구현 가능(삽입: append, 삭제: pop)
- 시간복잡도; O(1)


#큐(queue) 자료구조
- FIFO ; ex. 입구랑 출구가 모두 뚫려있는 터널
- from collections import deque(삽입: append, 삭제: popleft)
- 시간복잡도; O(1)


#재귀함수(recursive function)
- 자기 자신을 다시 호출하는 함수
- python 에서는 '최대 재귀 깊이 제한'이 있기 때문에 별다른 설정이 없다면 오류메세지와함께 종료되게 된다.
- 일반적인 문제풀이 경우(일부러 무한루프를 만들지 않는 경우)에는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
- 컴퓨터가 함수를 재귀적으로 호출하게 되면, 컴퓨터 메모리 내부의 스택 프레임에 쌓이게 된다.
=> 이러한 특징때문에 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 있다.
(ex. 단순히 더 짧고 간결하게 작성하기위해(dfs))



#DFS(Depth First Search)
- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- 스택 자료구조(or 재귀함수)를 이용한다.
=>  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면, 그 노드를 스택에 넣고 방문 처리를 한다.
       방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
       **즉, 매번 최상단 노드를 기준으로 방문하지 않은 인접노드가 있으면 그 인접한 노드로도 방문을 수행하는 것.
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

- 그래프 문제가 출제되면 노드의 번호가 1번부터 시작하는 경우가 많기 때문에 list의 0번 index는 비우고 index 1부터 시작하도록 한다.
'''



#재귀함수-팩토리얼 구현 예제(**참고; 수학적으로 0!과 1!의 값은 1이다.)
'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복구현: ', factorial_iterative(5))
print('재귀구현: ', factorial_recursive(5))
'''


#재귀함수 - 유클리드 호제법 예제
'''
def gcd(a,b):
    if a%b==0:      #a가 b의 배수라면
        return b    #b를 반환
    else:
        return gcd(b, a%b)      #b와 a를 b로 나눈 나머지의 최대공약수를 반환할 수 있도록 한다.

print(gcd(192, 162))
'''


#DFS 소스코드 예제
'''
def dfs(graph, v, visit):
    visit[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

dfs(graph, 1, visit)
'''