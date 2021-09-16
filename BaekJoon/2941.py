#크로아티아 알파벳(실5)
'''
**replace
문자열.replace(검색문자, '치환문자')


'''


import sys
s = sys.stdin.readline()    #입력시 문자열1개를 추가로 인식함 -> 왜...? => 문자열에 개행문자(\n ) 을 기본으로 추가인식하기 때문에
#s = input()

alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha_list:
    s = s.replace(i, '*')
print(s)
print(len(s))
