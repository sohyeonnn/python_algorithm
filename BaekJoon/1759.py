#암호 만들기(골5)
'''
최소 하나의 모음['a', 'e', 'i', 'o', 'u']
&
최소 두개의 자음
으로 만들 수 있는 암호의 조합을 생성
'''


#combinations 사용 sol
#30% 틀림 -> 마지막 조건 (len(alpha) - count >= 2)
#수정후 정답처리 -> (len(i) - count >= 2)
import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alpha = sorted(list(map(str, sys.stdin.readline().split())))

moum = ['a', 'e', 'i', 'o', 'u']


for i in combinations(alpha, L):
    count = 0
    for johap in i:
        if johap in moum:
            count += 1

    #최소 하나의 모음 and 자음이 2개 이상인것만 출력
    if (count >= 1) and (len(i) - count >= 2):
        print(''.join(i))