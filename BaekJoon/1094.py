#막대기_비트마스크(실4)

import sys
'''
#비트마스킹x 풀이
n = int(sys.stdin.readline())
stick = [64, 32, 16, 8, 4, 2, 1]
result = 0

for i in stick:
    while n-i >= 0:
        n -= i
        result += 1
print(result)
'''

#비트마스킹/1이 몇개인지 세는게 더 효율적인 풀이
n = int(sys.stdin.readline())

print(bin(n).count('1'))