#탐색알고리즘
'''
**순차(선형;linear)탐색; sequential search
- 리스트, 배열 내에서 특정 데이터를 찾기 위해 하나씩 차례대로 확인하는 방법
- 가장 흔하게 사용함
- 보통 정렬되지 않고 무작위로 주어진 데이터 내에서 특정 원소를 찾을 때 사용
- 시간복잡도; O(N)

**이진탐색(binary search)
- 배열 데이터가 정렬 되어있을 경우에만 사용이 가능하다.
=> 오름차순으로 정렬된 배열에서 원하는 숫자(target)을 찾는 알고리즘이다.

- 3가지 변수를 사용해서 구현되며, 배열의 시작점, 끝점, 중간점을 사용한다.
=>1. 배열 전체의 중간값을 target 값과 비교
=>2. 중간값이 target 값 보다 크면 왼쪽(작은쪽)부분만 선택
=>3. 왼쪽 부분의 중간값을 다시 target과 비교
==>값이 반씩 빠르게 줄어들게된다

- 시간복잡도; O(logN)
=>입력 데이터가 매우많거나 탐색 범위가 매우 넓을 때, 데이터 개수가 1000만다누이 이상, 1000억 이상일때 자주 사용
'''


#순차탐색
'''
import sys

array = [i for i in range(10, 30, 2)]       #list comprehension; [변수를 활용한 값 for 사용할 변수 이름 in 순회할 수 있는 값]
n = len(array)
target = int(sys.stdin.readline())

def sequential_search(n, target, array):        #n있어도되고 없어도되고
    for i in range(n):      #하나씩 target과 비교한다.
        if array[i] == target:      #배열의 요소가 target과 같다면,
            return i+1      #index가 아닌 몇번째 데이터인지 반환하기위해 인덱스에 +1해준다.


res = sequential_search(n, target, array)       #n있어도되고 없어도되고
print(f"{target} 데이터는 array의 {res}번째에 존재합니다!")
'''


#이진탐색

import sys
# 1. 재귀함수(def)로 구현
def binary_search(array, target, start, end):
    if start > end:
        return None

    middle = (start + end) // 2

    if array[middle] == target:
        return middle + 1
    elif array[middle] < target:
        return binary_search(array, target, middle+1, end)
    else:
        return binary_search(array, target, start, middle-1)

n, target = list(map(sys.stdin.readline().rstrip()))
array = list(map(sys.stdin.readline().rstrip()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("존재하는 원소가 없음")
else:
    print(result)




import sys
# 2.while 반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == target:
            return middle + 1
        elif array[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

n, target = list(map(int, sys.stdin.readline().rstrip()))
array = list(map(int, sys.stdin.readline().rstrip()))
#sys.stdin.readline()은 enter공백문자를 포함하기 때문에 꼭 rstrip()을 붙여주어야 한다.

result = binary_search(array, target, 0, n-1)
if result == None:
    print("존재하는 원소가 없습니다!")
else:
    print(result)