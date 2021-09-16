#크로아티아 알파벳(실5)
'''
**replace
문자열.replace(검색문자, '치환문자')
'''


import sys
#s = sys.stdin.readline()    #입력시 문자열1개를 추가로 인식함 -> 왜....?
s = input()

alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha_list:
    s = s.replace(i, '*')
print(s)
print(len(s))
