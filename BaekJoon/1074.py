#Z(실1)_재귀호출/분할정복
'''
**point
: 입력받은 크기에서 -> ... -> 2*2 사이즈가 될때까지 쪼개고
2*2 사이즈가 되면 찾고자하는 지점이 몇 사분면에 위치하는지 출력한다.

- 주어진 배열을 4등분 한다 -> '분할정복'
- 위의 과정을 반복하며 2*2가 되면 탐색을 시작한다 -> '재귀호출'
'''

import sys

N, r, c = map(int, sys.stdin.readline().split())

block = []
for i in range(int(2**N)):
    for j in range(int(2**N)):
        pass

def visit(x, y):

    #탐색 범위 벗어나는 경우 자동종료
    if x <= -1 or x >= 2**N or y <= -1 or y >= 2**N:
        return False

        # z모양으로 지나감
        visit(x, y)
        visit(x, y + 1)
        visit(x + 1, y)
        visit(x + 1, y + 1)
        return True


