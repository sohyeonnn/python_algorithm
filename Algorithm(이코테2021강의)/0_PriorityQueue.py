#우선순위 큐(Priority Queue)
'''
#자료구조별 특징
- 스택(stack, FILO); 가장 나중에 삽인된 데이터가 추출됨
- 큐(queue, FIFO); 가장 먼저 삽입된 데이터가 추출됨(공평한 자료구조라고도 함)
- 우선순위 큐(priority queue); 가장 우선수위가 높은 데이터가 추출됨



#우선순위 큐;
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

- 데이터를 우선순위에 따라 처리하고 싶을 때 사용
=> 물건데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우


#우선순위 큐 구현 방법
1) 리스트(list)를 이용하여 구현
2) 힙(heap) 자료구조를 이용하여 구현


#리스트 vs 힙 시간복잡도 비교
- 리스트; 삽입시간[ O(1) ] / 삭제시간[ O(n) ]
- 힙;    삽입시간[ O(longN) ] / 삭제시간[ O(longN) ]
=> 리스트의 삽입시간의 경우 단순히 뒤에 연달아 넣으면 되기 때문에 시간복잡도가 O(1)이 된 것
=> 리스트의 삭제시간의 경우 삭제하고자 할 때는 가장 우선순위가 높은 데이터를 찾아야 하기 때문에 선형적인 탐색시간이 소요된다.
=> 힙의 경우 데이터를 넣는것과 빼는것 모두 최악의 경우에도 [ O(longN) ]의 시간복잡도가 소요된다.

** 힙정렬; 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업 그 자체로서 정렬이 수행된다는 것이 특징임
    => 이 경우 시간복잡도는 [ O(NlogN) ]


#힙(heap)의 특징
- *완전 이진 트리 자료구조이다
- 일종의 트리 자료구조로 -> 항상 루트노드(root node)를 제거하는 방식으로 동작한다.
1)최소 힙(min heap);               ->      Python에서는 최소 힙 형태로 동작(기본정렬; 오름차순)
- 루트 노드가 가장 작은 값을 가진다.
- 따라서 값이 가장 작은 데이터가 우선적으로 제거된다.
2)최대 힙(max heap);               ->      Python에서 max heap 형태로 동작하는 힙 자료구조가 필요하다면, 데이터를 넣을때와 꺼낼 때 '-'를 붙여주면 됨
- 루트 노드가 가장 큰 값을 가진다.
- 따라서 값이 큰 데이터가 우선적으로 제거된다.

    *완전 이진 트리(complete binary tree)
    - 루트(root) 노트부터 시작하여 -> 왼쪽 자식노드 -> 오른쪽 자식 노드
    순으로 데이터가 차례대로 삽입되는 트리(tree)를 의미한다.



#힙 구현
- 최소 힙 구성  함수; Min-Heapify()
=> (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 부모와 위치를 교체한다

- 힙에 새로운 원소가 삽일될 때;
=> 새로운 원소가 삽입되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.

- 힙에서 원소가 제거될 때;
=> 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
=> 1) 원소를 제거할 때는 가장 마지막 노드가 루트 노드(제거하고자 하는 노드)의 위치에 오도록 한다.
   2) 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행한다.
'''


#우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
'''
import sys
import heapq
input = sys.stdin.readline()

#리스트나 튜플같은 하나의 iterable한 객체가 들어옴
def heapsort(iterable):
    h = []
    result = []

    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:

        # heappush() 함수를 이용하여 힙에 원소를 추가할 수 있음,
        # heappush(h, value) -> h는 원소를 추가할 대상 리스트/value는 추가할 원소를 넘긴다.
        heapq.heappush(h, value)    #max heap 형태가 필요하다면 데이터를 '-' 형태로 넣음

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))     #max heap 형태가 필요하다면 데이터를 '-' 형태로 꺼냄
    return result

n = int(input)
arr = []

for i in range(n):
    arr.append(int(input))

res = heapsort(arr)

for i in range(n):
    print(res[i])       #오름차순 정렬 형태로 출력
'''


#힙정렬
import heapq

def heap_sort(nums):
    heap = []
    for num in nums:

        # num 을 heap 에 추가
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return  sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))