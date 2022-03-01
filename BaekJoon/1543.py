#문서 검색(실4)_그리디
'''
문자열, 그리디

문서와 검색하려는 단어가 주어졌을 때, 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 문제
->즉, 12345 에서 123이 345가 해당 단어이면 1번만 검색되는 것(중복허용x 이기 때문에)

sol1.
monseo앞에서부터 word를 거쳐서 몇번 등장하는지 count
-> 인덱스 번호 변수를 생성하여 중복되지 않게 차례대로 단어의 개수를 세면된다.

sol2.
count 함수 사용
'''
import sys
input = sys.stdin.readline

munseo = str(input().rstrip())
word = str(input().rstrip())

count = 0

result = munseo.count(word)
print(result)