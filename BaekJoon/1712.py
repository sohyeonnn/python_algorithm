#손익분기점(브4)
'''
가변비용이 노트북 가격보다 크거나 같으면 손익분기점이 발생하지 못한다.

=>시간제한때문에 반복문으로 풀면 타임오버
'''
'''
- input() = sys.stdin.readline()
- 여러개 정수를 입력바등려면 map 함수를 사용한다.
- rstrip(); 인자로 받은 문자를 string의 오른쪽에서 제거
'''

import sys
#A, B, C = list(map(int, input().split()))
A, B, C = map(int, sys.stdin.readline().split())


if B >= C:
    print(-1)
else:
    print(int(A/(C-B)) +1)     #+1해주는 이유는 '손익분기점을 만족하는 첫번째'를 출력해야하기 때문에
