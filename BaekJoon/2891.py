#카약과 강풍(실5)-그리디
'''
*Q
자신의 바로 다음이나 전에 경기하는 팀에게만카약을 빌려준다.
팀4는 팀3 or팀5에만 빌려줄 수 있음. 다른 팀에게서 받은 카약은 또 다른팀에게 빌려줄 수 없음.
- 이때 카약을 적절히 빌렸을 때 출발하지 못하는 팀의 최솟값을 몇팀인가?

sol1.
n입력대로 1~n크기에 1이 담겨있는 배열을 만들고
s_number에 해당되는 수에서는 -1 해준다
r_number에 해당된느 수에서는 +1 해준다.

=> sol1을 더 간단히 생각해야함

*point
구하고자 하는 값 = 출발하지 못하는 팀 수
즉, 출발하지 못하는 팀은 무조건 카약이 손상된 팀중에 있기 때문에 손상된 팀 번호 리스트를 검사해야함.
카약이 손상된 팀 앞, 뒤의 카약이 남는 팀 리스트에 포함되어 있으면 카약을 빌려 출발할 수 있고, 남는 팀 리스트에서 해당 팀을 삭제한다.

**list.remove
'''

import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
broken_number = list(map(int, input().split()))
extra_number = list(map(int, input().split()))

result = 0
for i in broken_number:
    if i - 1 in extra_number:
        extra_number.remove(i - 1)
    elif i + 1 in extra_number:
        extra_number.remove(i + 1)
    else:
        result += 1

print(result)