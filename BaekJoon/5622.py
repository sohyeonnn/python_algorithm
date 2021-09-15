#다이얼(브2)
'''
- sys.stdin.readline()으로 입력받을것
- Number 리스트 만들어서
'''
import sys
alpha = sys.stdin.readline()
alpha_list = list(alpha)

Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sec = 0

for i in alpha_list:
    for j in Number:
        if i in j:
            sec += Number.index(j) + 3
print(sec)