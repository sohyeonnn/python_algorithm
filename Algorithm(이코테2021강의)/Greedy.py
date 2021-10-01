#탐욕법
'''
#1
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 정당성 분석이 중요
=> 문제에서 요구하는 최적의 해를 구할 수 있는지 검토하는 것이 중요하다.

#2
- 내 상황에서 가장 큰값을 고르는 알고리즘이라고 볼 수 있다.

#3
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다.
- 코딩테스트에서는 그리디알고리즘, 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서 출제하는 경우가 많다.
'''


#거스름돈
'''
n = int(input())    #1260원 일 때
count = 0

array = [500, 100, 50, 10]

for i in array:     #화폐의 종류만큼 for문이 반복된다.
    count += n // i     #1. 500원으로 2번만큼 거슬러줄 수 있다.
    n %= i              #1. 나누어서 260을 남긴다.

print(count)
'''


#1이 될 때까지
'''
import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

while True:
    target = (n // k) * k       #n이 k로 나누어 떨어지는 수가 될 때 까지 빼기
    count += n - target

    n = target

    if n < k:       #n이 k보다 작을 때(더이상 나눌 수 없을 때)반복문을 탈출한다.
        break

    count += 1      #그렇지 않다면
    n //= k

count += n - 1      #마지막으로 남은 수에 대해 1씩 뺀다.
print(count)
'''


#곱하기 혹은 더하기
'''
import sys
s = list(sys.stdin.readline().rstrip())
result = int(s[0])      #입력받은 str을 int로 변경

for i in range(len(s)):
    num = int(s[i])

    if num <= 1 or result <= 1:       #s[i]가 0 인 경우
        result += num   #+ 연산을 해준다.
    else:
        result *= num
print(result)
'''


#모험가 길드
'''
풀이과정
1. 입력받은 모험가의공포도를 오름차순 정렬한다.
2. 앞에서부터 공포도를 확인하며 현재 그룹에 포함된 모험가의 수가 현재 확인하고있는 공포도
보다 크거나 같다면 이를 그룹으로 설정하면 된다.
3. 공포도가 오름차순으로 정렬되어있어서 항상 최소한의 모험가의 수만 포함해서 그룹을 결성한다.
'''
import sys

n = int(sys.stdin.readline().rstrip())      #모험가 수

x = list(map(int, input().split()))        #모험가의 공포도
x.sort()    #오름차순 정렬

result = 0  #총 그룹의 수
count = 0   #현재 그룹에 포함된 모험가의 수

for i in x:     #오름차순으로 공포도를 낮은 것 부터 하나씩 확인
    count += 1      #현재 그룹에 해당 모험가를 포함시킨다.
    if count >= i:      #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1     #총 그룹의 수 증가
        count = 0       #현재 그룹에 포함된 모험가의 수 초기화

print(result)

