#Z(실1)_재귀호출/분할정복
'''
**point
: 입력받은 크기에서 -> ... -> 2*2 사이즈가 될때까지 쪼개고
2*2 사이즈가 되면 찾고자하는 지점이 몇 사분면에 위치하는지 출력한다.
- 주어진 배열을 4등분 한다 -> '분할정복'
- 위의 과정을 반복하며 2*2가 되면 탐색을 시작한다 -> '재귀호출'

**생각한 풀이(21.12.16 retry)
list를 만들어서 좌표에 해당하는 값을 찾는식으로 생각해봤는데 n은 15까지 가능하다
=> 2**15 x 2**15 .....? 절대아님



**찾아본 풀이(21.12.16 retry)
    [step1] 현재 행렬 형태 중에 4등분 했을때 r, c는 몇 번째일지 구한다.
    [step2] 그렇게 몇번째인지 구한 다음, r과 c, 시작점(res)를 업데이트 해준다.
            n을 1 빼준다.
    [step3] step1,2를 반복하며 n이 1이 될 때 까지 반복한다.
    [step4] r, c를 이용해서 최종적으로 구한다.

**풀이법 블로그
: https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-1074%EB%B2%88-Z-1-Python
'''

import sys

n, r, c = map(int, sys.stdin.readline().split())

res = 0

while n != 0:
    ran = 2 ** (n-1)    #4등분 중 몇번째 위치인지

    if r >= ran:
        if c >= ran:    #4번째
            res += (4 ** (n-1)) * 3
            r -= ran
            c -= ran
        else:           #3번째
            res += (4 ** (n - 1)) * 2
            r -= ran

    else:
        if c >= ran:    #2번째
            res += (4 ** (n - 1)) * 1
            c -= ran
        else:           #1번째
            pass
    n -= 1      #n이 0이 될 때 까지 반복


if r == 0:
    if c == 0:
        print(res)
    else:
        print(res + 1)
else:
    if c == 0:
        print(res + 2)
    else:
        print(res + 3)