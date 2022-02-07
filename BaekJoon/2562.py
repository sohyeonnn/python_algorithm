#최댓값(브2)
'''
리스트의 특정 원소 인덱스 출력 방법
: list.index()
'''

import sys
input = sys.stdin.readline

number = []
for i in range(9):
    n = int(input())
    number.append(n)

number_max = max(number)
print(number_max)
print(number.index(number_max)+1)