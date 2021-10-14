#하노이 탑 이동 순서(실2)_재귀함수
'''
**재귀함수(하노이탑)

n개의 원반을 특정 기둥으로 옮기려면
맨 아래를 제외한 원반들을 다른 기둥으로 옮기고
맨 아래 원반을 목적지 기둥으로 옮기고
다른 기둥에 옮겼던 원반들을 그 위에 얹는다.

원반 총 갯수가 홀/짝이냐에 따라
시작할 때 맨 위 원반을
=> 목표 기둥에 놓을것인가 or 다른 기둥에 놓을 것인가가 결정된다.


*참고강의;
https://www.youtube.com/watch?v=aPYE0anPZqI
'''

import sys

n = int(sys.stdin.readline().rstrip())


def hanoi(n, start, fin, other):#원반개수, 출발지기둥번호, 목적지기둥번호, 나머지기둥번호

    if n < 2:       #n=1은 어차피 바로 이동
        print(start, fin)
        return

    hanoi(n-1, start, other, fin)
    print(start, fin)
    hanoi(n-1, other, fin, start)

print((2**n)-1)     #총이동수

hanoi(n, 1, 3, 2)


