#덱(실4)
'''
deque; double ended queue를 뜻함,
데이터를 양방향에서 추가하고 제거할 수 있는 자료구조이다.
'''

from collections import deque
import sys

n = int(sys.stdin.readline())

d = deque([])

for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == 'push_back':
        d.append(s[1])

    elif s[0] == 'push_front':
        d.appendleft(s[1])

    elif s[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print('-1')

    elif s[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print('-1')

    elif s[0] == 'size':
        print(len(d))

    elif s[0] == 'empty':
        if d:
            print('0')
        else:
            print('1')

    elif s[0] == 'front':
        if d:
            print(d[0])
        else:
            print('-1')

    elif s[0] == 'back':
        if d:
            print(d[-1])
        else:
            print('-1')