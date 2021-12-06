#이진 탐색, 파라메트릭 서치
'''
#순차 탐색
: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
    =>가장 기본적인 형태의 데이터 탐색 알고리즘


#이진 탐색
: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    => log시간의 시간복잡도를 가질 수 있음
    => 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

#이진 탐색 시간복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 logN 에 비례한다
    =>이상적인 경우 한 번 연산을 수행할 때 마다 절반에 가깝게 줄어들기 때문
- 이진 탐색은 탐색 범위를 절반씩 줄이며 시간복잡도는 [ O(logN) ] 을 보장한다.

#python 이진 탐색 라이브러리
- bisect_left(a, x): 정렬된 순서를 유지하며 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하며 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
    => 값이 특정 범위에 속하는 데이터 개수를 구할 수 있음


#파라메트릭 서치(parametric search)
- 파라메트릭 서치란 *최적화 문제를 결정 문제(예 or 아니오)로 바꾸어 해결하는 기법이다.
    *최적회문제란?; 어떤 함수의 값을 최대한 낮추거나 높이는 문제
    => ex. 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코테에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음
'''


#def구현
'''
import sys
n, target = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

#target; 찾고자하는 데이터
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # 중간점을 명시해줌
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자하는 값이 작은 경우, 중간점 위치를 포함해 즉 우측에 위치한 값들은 항상 타겟보다 큰 값들이 존재함
    elif array[mid] > target:
        #끝점(mid - 1)을 중간점 왼쪽으로 옮겨서 왼쪽 부부넹 대해서 다시 탐색을 수행하도록 만들어준다.
        return binary_search(array, target, start, mid - 1)
    else:
        #오른쪽을 확인하게 만들기 위해서 시작점을 mid + 1로 옮기는 것이다.
        return binary_search(array, target, mid + 1, end)


result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)#해당 원소가 존제하는 인덱스 값을 출력(인덱스+1로 출력해서 몇 번째 원소인지 출력한다)
'''


#반복문 구현
'''
import sys
n, target = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            mid = end - 1
        else:
            mid = end + 1
    return None

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소없음")
else:
    print(result + 1)
'''


#떡볶이 떡 만들기
'''
import sys

n, m = list(map(int, sys.stdin.readline().split()))
dduk = list(map(int, sys.stdin.readline().split()))

#처음 시작값 설정
start = 0
end = max(dduk)

result = 0
while(start <= end):
    total_dduk_height = 0
    cut_height = (start + end) // 2

    for i in dduk:
        #잘랐을 때의 떡의 양 계산
        if i > cut_height:
            total_dduk_height += i - cut_height
    #떡의 양이 원하는 양(m) 보다 부족한 경우 더 많이 자르기(왼쪽 부분을 탐색)
    if total_dduk_height < m:
        end = cut_height - 1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        #최대한 덜 잘랐을때를 구한는 것이므로 result에 기록한다
        result = cut_height 
        start = cut_height + 1

print(result)
'''


#정렬된 배열에서 특정 수의 개수 구하기
'''
import sys

n, x = list(map(int, sys.stdin.readline().split()))
list_n = list(map(int, sys.stdin.readline().split()))

X = list_n.count(x)
print(X)
'''

from bisect import bisect_left, bisect_right
import sys

n, x = list(map(int, sys.stdin.readline().split()))
list_n = list(map(int, sys.stdin.readline().split()))

#값이 left_value이상, right_value이하인 데이터의 모두 찾을 수 있음
def count_by_range(list_n, left_value, right_value):
    left_index = bisect_left(list_n, left_value)
    right_index = bisect_right(list_n, right_value)
    return right_index - left_index

#값이 x인 데이터를 세고싶은 것이기 때문에 x이상 x이하로 범위를 잡고 데이터의 개수를 계산해준다.
count = count_by_range(list_n, x, x)

if count == 0:
    print(-1)
else:
    print(count)