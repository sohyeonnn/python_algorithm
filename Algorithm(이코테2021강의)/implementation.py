#구현(시물레이션과 완전탐색)
'''
- 구현; 머리속에있는 알고리즘을 소스코드로 바꾸는 과정
- 구현 유형의 문제란?
=> 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 뜻함

- 일반적으로 알고리즘 문제에서의 2차원 공간은 '행렬(matrix)'의 의미로 사용된다.
=> 행렬에서는 왼쪽상단이 (0, 0) 지점이다.

- 시물레이션 및 완전탐색 문제에서는 2차원 공간에서의 '방향 벡터'가 자주 활용돤다.
=> 세로축; x(위 방향;- / 아래 방향; +), 가로축; y(좌; - / 우; +)
'''


#상하좌우
'''
n = int(input())

plan = input().split()

x, y = 1, 1     #현재위치

#방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

#계획서에 적혀있는 이동 계획을하나씩 확인
for i in plan:

    #이동 후 좌표를 설정할 수 있도록 한다.
    for j in range(len(move_type)):     #좌우상하만큼 반복
        if i == move_type[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    #공간을 벗어나지 않는 경우 이동을 수행한다.
    x, y = nx, ny

print(x, y)
'''


#시각(완전탐색; 브루트포스)
'''
h = int(input())

count = 0

for i in range(h+1):    #시
    for m in range(60):     #분
        for s in range(60):     #초
            time = str(i) + str(m) + str(s)     #시각
            if '3' in time:     #시각안에 3이 포함된다면,
                count += 1      #카운트를 증가시킴
print(count)
'''


#왕실의 나이트(구현, 완전탐색(브루트포스))
'''
행렬의 사이즈, (x, y)를 구현하려했으나 옳지못한 방법

data = input()
row = int(data[0])
column = int(ord(data[1])-int(ord('a'))+1)

#dx, dy를 사용하지않고 하나의 리스트로 사용 가능
night_dir = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

count = 0

for night in night_dir:
    next_row = row + night[0]
    next_column = column + night[1]

    #8*8짜리 판 안에 있다면
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:

        #결과값을 증가시킨다.
        count +=1

print(count)
'''


#문자열 재정렬

s = input()

s1 = list(s)

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

hap = 0
for i in s1:
    for n in number:
        hap += int(i)
    result = sorted(s1)
print(result, hap)