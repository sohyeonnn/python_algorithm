#단지번호붙이기(실1)_dfs
'''
1; 집이 있는 곳
0; 집이 없는 곳
연결된 집의 모임인 단지를 정의하고 단지에 번호를 붙이려 한다.

지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하시오.

*point
-음료수 얼려먹는 문제 유형

*global 전역변수 사용
'''
'''
#음료수 얼려먹기 참고한 코드
import sys
input = sys.stdin.readline

n = int(input().rstrip())

apt = []
for i in range(n):
    apt.append(list(map(int, input().rstrip())))


def dfs(x, y):
    #범위를 벗어나는 경우 종료조건 설정
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    #탐색하는 원소가 1인 경우(아파트 단지를 생성할 수 있는 경우), 현재 위치를 아직 방문하지 않았다면
    if apt[x][y] == 1:
        global count    #global 전역변수 선언(아파트 수 세어주기 위함)
        count += 1      #이어진 집들끼리 count해준다, 123456712345678...

        apt[x][y] = -1  #방문처리

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)   #현재 노드와 연결된 모든 인접 노드를 방문한다

        return True
    return False    #1이 아닌 부분에서는 False를 반환하게 함


num = []
global count
count = 0
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:   #만약 해당 위치에서 dfs수행해서 방문처리가 됐다면, count한다.
            num.append(count)

            result += 1  #방문처리가 이루어지는 부분에서만 count를 수행한다
            count = 0   #단지 각각의 합을 알기 위한 것이므로 한 단지의 합을 구한 뒤에는 count를 0으로 초기화해준다
print(result)   #총 단지 수

num.sort()
for i in num:   #한 줄씩 출력
    print(i)
'''
#상하좌우이동코드 바꾼거
import sys
input = sys.stdin.readline

n = int(input().rstrip())

apt = []
for i in range(n):
    apt.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count  # global 전역변수 선언(아파트 수 세어주기 위함)

    if x <= -1 or x >= n or y <= -1 or y >= n:  #범위를 벗어나는 경우 종료조건 설정
        return False

    #탐색하는 원소가 1인 경우(아파트 단지를 생성할 수 있는 경우), 현재 위치를 아직 방문하지 않았다면
    if apt[x][y] == 1:
        count += 1      #이어진 집들끼리 count해준다, 123456712345678...

        apt[x][y] = -1  #방문처리

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx, ny)

        return True
    return False    #1이 아닌 부분에서는 False를 반환하게 함


num = []
global count
count = 0
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:   #만약 해당 위치에서 dfs수행해서 방문처리가 됐다면, count한다.
            num.append(count)

            result += 1  #방문처리가 이루어지는 부분에서만 count를 수행한다
            count = 0   #단지 각각의 합을 알기 위한 것이므로 한 단지의 합을 구한 뒤에는 count를 0으로 초기화해준다
print(result)   #총 단지 수

num.sort()
for i in num:   #한 줄씩 출력
    print(i)