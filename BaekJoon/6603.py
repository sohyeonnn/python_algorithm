#로또(실2)
'''
int형으로 구성된 list를 join하려고하면 Typeerror가 발생한다.
    해결=> join(map(str, _)) 로 str형으로 바꿔서 해결한다.
'''

#itertools풀이
'''
import sys
from itertools import combinations

while True:
    s = list(map(int, sys.stdin.readline().split()))

    if s[0] == 0:
        break

    for i in combinations(s[1:], 6):
        com = list(i)
        print(" ".join(map(str, com)))
    print()
'''

#다른풀이 도전
'''
import sys

while True:
    s = list(map(int, sys.stdin.readline().split()))

    if s[0] == 0:
        break

    com = []
    com.append(s[1:])
    for i in range(s[0]):
'''