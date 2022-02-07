#약수(실5)
'''
첫째줄: n의 진짜 약수의 개수
둘째줄: n의 진짜 약수(중복x)

풀이방법
=> 약수에서 1과 자기자신을 제외했으므로 약수중 최소값과 최대값을 곱하면 된다.
'''

import sys
input = sys.stdin.readline

n = int(input())
yaksu = list(map(int, input().split()))

yaksu_min = min(yaksu)
yaksu_max = max(yaksu)

result = yaksu_min * yaksu_max
print(result)