#Project Teams(실4)_그리디
'''
프로젝트 팀하나는 두 명의 학생으로 구성,
각 학생은 한 팀의 팀원이어야함.

예를 들어, 학생들의 코딩 역량이 {1, 7, 5, 8}로 주어졌다면
(8, 1), (7, 5)로 2개의 조를 짤 수 있으며 프로그램은 9를 출력해야 한다.
=> 팀들의 코딩역량 합 중 최소값을 출력

sol1.
팀 수 대로 list로 분할하되,
첫번째 리스트(팀)에 입력의 min과 max
두번째 리스트(팀)에 남은 값의 min과 max
...
순으로 분할하여 list 내부의 합이 가장 작은 것을 출력한다.

*point
각 학생들의 점수를 입력받은 후 오름차순 정렬을 한다.
모든 페어(팀)의 차이를 최소화 하기 위해 (가장왼쪽(작은값), 가장오른쪽(큰값))식으로 팀을 만든다.
팀 중 합이 최소가 되는 것을 출력한다.
=> sol1과 아이디어는 동일, 하지만 sol1은 구현이 불가능하다. 이것을 sort를 이용하여 구현한다는 것을 기억하기.
'''

import sys
input = sys.stdin.readline

n = int(input())
coding_level = list(map(int, input().split()))
coding_level.sort()

team = []

for i in range(len(coding_level)):
    team.append(coding_level[i] + coding_level[len(coding_level)-1-i])
print(min(team))