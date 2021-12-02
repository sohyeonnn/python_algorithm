#정렬(Sorting)
'''
#정렬
- 정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.


##선택 정렬(selection sort)
- 처리되지 않은 데이터 중, 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
    => 매번 현재 데이터 중 가장 작은 데이터를 골라서 앞쪽으로 보내주는 것
- 탐색 범위는 정렬을 수행할수록 줄어들게 된다
- 2중 for문을 이용해서 구현할 수 있음

#선택 정렬의 시간 복잡도
- N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
- N + (N-1) + (N-2) + ... + 2
    => O(N**2)



##삽입 정렬(insertion sort)
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
- 선택정렬에 비해 일반적으로 더 효율적으로 동작한다.

#삽입 정렬의 시간 복잡도
- 시간복잡도는 [ O(N**2) ] 이며, 2중 for문으로 사용된다.
- 현재 리스트의 데이터가 거의 정렬되어있는 상태라면 매우 빠르게 동작한다.
    => 그래서 최선의 경우(이미 모든 데이터가 다 정렬되어있는 경우)의 시간복잡도는 [ O(N)] 이다.



##퀵 정렬(quick sort)
- 기준 데이터를 고른 뒤, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 가장 많이 사용되는 정렬 알고리즘 중 하나이다.
- 병합 정렬(merge sort)과 더불어 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이다.
- 가장 기본적인 형태의 퀵 정렬의 경우 첫 번째 데이터를 기준 데이터(pivot)로 설정한다.
    => [step1] 왼쪽에서는 pivot값보다 큰 데이터를 고르고, 오른쪽에서는 pivot 값보다 작은 데이터를 고른다.
       [step2] 각각 골라진 데이터의 위치를 서로 바꿔준다.
       [step3] step1, 2를 반복한다.
       [step4] 반복하다 데이터의 위치가 서로 엇갈리는(-> <-) 경우, 작은 데이터와 pivot값의 위치를 바꿔준다.
       [step5] 기존의 pivot값이 중앙으로 들어가게 되고, 이것을 기준으로 왼쪽은 기존pivot보다 작은값, 오른쪽은 기존 pivot보다 큰값으로 나뉘게 된다.
                => 이러한 작업을 분할(divide) 라고 한다.
       [step6] 왼쪽, 오른쪽에 있는 데이터들에 대해 각각 마찬가지로 quick정렬을 수행해준다.

#퀵 정렬이 빠른 이유?
- 분할이 [ 8 -> 4 -> 2 -> 1 ] 과 같이 절반씩 일어난다면 전체 연산 횟수로 O(logN)를 기대할 수 있다.

#퀵 정렬의 시간 복잡도
- O(NlogN)
- 최악의 경우 O(N**2)의 시간 복잡도를 가진다.
    => 분할이 절반에 가깝게 이루어지지않고, 한쪽에 편향되어 이루어지면 이런 경우가 발생할 수 있음



##계수 정렬(counting sort)
- 특정 조건에서만 사용가능하지만 매우 빠르게 동작하는 정렬 알고리즘
    =>데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용할 수 있다.

#계수 정렬의 복잡도
- 시간 공간 복잡도 모두 [ O(N+K) ] 이다.
- 계수정렬은 데이터의 범위가 너무 크거나 그 공백이 너무 큰 경우 심각한 비효율성을 초래할 수 있다.
    => ex) 0, 999999로 2개의 데이터가 주어지는 경우 1000000의 리스트를 만들어야함
- 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있음
    => ex) 성적에 따른 학생 분류 등
'''


#선택정렬
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(arr)
for i in range(len(arr)):   #i는 가장 작은 데이터와 위치가 바뀔 인덱스를 의미함
    min_index = i   #가장 작은 원소의 인덱스를 고름
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:     #현재 가장 작은 원소보다 더작은 원소가 있다면,
            min_index = j   #그 위치 인덱스 값을 min_index에 담아줌
        arr[i], arr[min_index] = arr[min_index], arr[i]     #가장 앞쪽 원소와 가장 작은 원소의 인덱스를 서로 바꿔줌
    print(arr)
print(arr)
'''

#삽입정렬
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(arr)
print(arr)
for i in range(1, n):   #두번째 원소부터 시작해서 왼쪽으로 이동해나가면서 위치를 바꿔주는 방식
    for j in range(i, 0, -1):   #j는 삽입하고자하는 원소의 위치를 의미함
        if arr[j] < arr[j-1]:   #왼쪽에있는 원소와 비교했을 때 자신이[j] 더 작다면
            arr[j], arr[j-1] =arr[j-1], arr[j]      #위치를 바꿔준다
        else:   #비교했을때 자신보다 크거나 같다면 그대로 냅두면 됨
            break
    print(arr)
print(arr)
'''

#퀵 정렬1
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(arr)
def quick(arr, start, end):
    if start >= end:
        return

    pivot = start   #첫 번째 원소를 pivot값으로 설정함
    left = start + 1    #첫 번째를 제외한 나머지 원소중 제일 왼쪽을 left
    right = end         #가장 오른쪽을 right로 설정해줌
    while left <= right:    #left가 가리키는 인덱스보다 right가 가리키는 인덱스가 더 작다면 엇갈린 것이라고 판단
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick(arr, start, right-1)
    quick(arr, right+1, end)

quick(arr, 0, len(arr) - 1)
print(arr)


#퀵정렬2_(list comprehension)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    #리스트 컴프리헨션
    left_side = [x for x in tail if x <= pivot]     #pivot을 제외한 리스트의 원소를 하나하나 확인하며 pivot보다 작으면 왼쪽 리스트에 담아준다
    right_side = [x for x in tail if x > pivot]

    return quick(left_side) + [pivot] + quick(right_side)

print(quick(arr))
'''

#계수정렬
'''
arr = [7, 5, 9, 0, 3, 1, 7, 5, 9, 1, 6, 2, 4, 8]

#모든 범위를 포함하는 크기의 리스트를 만든다, 모든 값은 0으로 초기화해준다.
count = [0] * (max(arr) + 1)

for i in range(len(arr)):   #데이터를 하나씩 확인
    count[arr[i]] += 1  #각 데이터에 해당하는 인덱스의 값을 1씩 증가시킴, 각 데이터가 몇 번씩 등장했는지 count 배열에 기록함

for i in range(len(count)):     #각각의 인덱스를 0~9까지 확인
    for j in range(count[i]):   #각 인덱스를 값으로 가지는 값이 몇 번씩 등장했는지를 출력
        print(i, end=' ')
'''


#문제_ 두 배열의 원소 교체
import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()    #오름차순
b.sort(reverse = True)      #내림차순

#a[0:k], b[0:k] = b[0:k], a[0:k]

for i in range(k):      #두 배열의 원소를 최대 k번 비교
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
