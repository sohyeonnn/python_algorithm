#큐2(실4)
'''
FIFO; first in first out
즉 선입선출
deque; 데크, 일반 큐와 달리 앞과 뒤 모두에서 데이터의 삽입과 삭제가 일어난다.
연결리스트로 구현되어있어 삽입과 삭제가 O(1)안에 끝나 매우 빠르다.
'''

from collections import deque
import sys
n = int(sys.stdin.readline())

queue = deque([])

for s in range(n):
    i = sys.stdin.readline().split()

    if i[0] == 'push':
        queue.append(int(i[1]))

    elif i[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif i[0] == 'size':
        print(len(queue))

    elif i[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif i[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif i[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
