#정렬알고리즘
'''
정렬 알고리즘은 시간 복잡도에 따라 성능을 좌우하며, 성능이 좋을수록 구현방법이 어려워진다.
-> 시간복잡도가 적을수록 구현이 어려워진다.

**버블정렬
- 인접한 두 수를 비교해 나간다
- 시간복잡도; O(n**2)
- 앞/뒤에서부터 시작하여 큰수/작은수를 뒤로 보내며 완성해나간다.

**선택정렬
- 한바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환한다.
- 시간복잡도; O(n**2)
- 앞에서부터 정렬해나간다.

**삽입정렬
- 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
=> 모든 요소를 앞에서부터 정렬 범위를 확장시켜나가며 정렬을 진행한다.
- 시간복잡도; O(n**2)
- 버블, 선택 정렬과는 다르게 정렬이 진행될수록 비교 범위가 넓어진다.

-----

**병합정렬
- 분할 정복과(divide&conquer) *재귀(함수가 자기자신을 호출)를 이용한 알고리즘
=> 주어진 배열의 크기가 1이 될 때 까지 반씩 쪼갠 뒤 정렬을 진행, 병합을 진행한다.
- 시간복잡도; O(NlogN)
- 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬하게 된다.
=> 이 과정에서 두개의 공간이 필요함
- 다른 정렬 알고리즘과는 다르게 인접한 값들 간의 상호 자리 교대(swap)가 일어나지 않는다.

(*재귀함수)
- 자기 자신을 호출하는 함수
- 쉽게말해 def 형태를 뜻한다.

**퀵정렬
- 분할정복 알고리즘
- 시간복잡도; O(NlogN)
- 추가적인 메모리 공간이 필요 없다
- 병합정렬은 균등하게 분할했다면, 퀵정렬은 Pivot(정렬을 위해 사용하는 임의의 기준값)을 설정하고 그것을 기준으로 정렬한다.

=> python에서의 sort()같은 함수는 대부분 퀵정렬을 기본으로한다.
'''


#버블정렬(Bubble sort)
'''
bubble = [9,8,7,6,5,4,3,2,1]

def BubbleSort(bubble):
    n = len(bubble)

    for i in range(n):
        for j in range(n-i-1):
            if bubble[j] > bubble[j+1]:
                bubble[j], bubble[j+1] = bubble[j+1], bubble[j]

        print(bubble)       #정렬되는 과정
print("버블정렬: ", bubble)
BubbleSort(bubble)

print("결과: ", bubble)   #버블정렬된 결과
'''


#선택정렬(selection sort)
'''
select = [8,4,5,6,7,9,3,1,2]

def SelectionSort(select):
    n = len(select)

    for i in range(n):
        min_index = i       #최소값을 저장할 변수에 i를 초기화시킨다.

        for j in range(i+1, n):     #현재 index부터 마지막 index까지 최소값을 찾아낸다
            if select[min_index] > select[j]:       #최소값의 인덱스가 현재값보다 크면,(최소값을 찾아내면)
                min_index = j       #최소값의 index를 가져온다.

        select[i], select[min_index] = select[min_index], select[i]
        #(찾아낸 최소값의 index와 현재 index에 있는 값을 swap한다.)

        print(select)

print("선택정렬(오름차순): ", select)
SelectionSort(select)
print("결과: ", select)
'''


#삽입정렬(insertion sort)
'''
insert = [8,4,6,2,9,1,3,7,5]

def InsertionSort(insert):
    n = len(insert)

    for i in range(n):      #순방향 진행
        for j in range(i , 0, -1):      #역방향 진행
            if insert[j-1] > insert[j]:
                insert[j-1], insert[j] = insert[j], insert[j-1]

        print(insert[:i+1])     #정렬되는 순서대로 볼 수 있음

print("삽입정렬: ", insert)
InsertionSort(insert)
print("결과: ", insert)
'''


#합병정렬(merge sort)
'''
merge = [8,4,6,2,9,1,3,7,5]

def merge_sort(merge):

    if len(merge) < 2:       #merge의 길이가 2보다 작다면,
        return merge

    mid = len(merge) // 2       #8 -> 4 -> 2-> 1 로 나누면서 비교하기
    low_merge = merge_sort(merge[:mid])
    high_merge = merge_sort(merge[mid:])

    merged_arr = []
    l = h = 0

    while l < len(low_merge) and h < len(high_merge):
        if low_merge[l] < high_merge[h]:
            merged_arr.append(low_merge[l])
            l += 1

        else:
            merged_arr.append(high_merge[h])
            h += 1

    merged_arr += low_merge[l:]
    merged_arr += high_merge[h:]
    print(merged_arr)
    return merged_arr

print("합병정렬: ", merge)
merge = merge_sort(merge)
print("결과: ", merge)
'''


#퀵정렬(Quick Sort)

quick = [8,4,6,2,5,1,3,7,9]

def QuickSort(quick):
    if len(quick) <= 1:
        return quick

    pivot = len(quick) // 2

    front_arr, pivot_arr, back_arr = [], [], []
    for i in quick:
        if i < quick[pivot]:
            front_arr.append(i)
        elif i > quick[pivot]:
            back_arr.append(i)
        else:
            pivot_arr.append(i)

    print(front_arr, pivot_arr, back_arr)
    return QuickSort(front_arr) + QuickSort(pivot_arr) + QuickSort(back_arr)
    # + 로 이어줘서 한 list안에 나오게 해줌 / , 로 이어주면 빈공간까지 출력된다.

print("퀵정렬: ", quick)
quick = QuickSort(quick)
print("결과: ", quick)
