#level2_완탐
'''
split 으로 분리
itertools로 가능한 모든 경우의 수의 조합/순열 을 구한 뒤
join 으로 합침
소수 = 나누어 떨어지는 값이 1 과 자기자신밖에 없는 값
-> 이라는 if문을 만들어 만족하면 count +=1 해주는 식으로 답을 찾는다.

*point
1.split은 문자열 사이의 공백을 기준으로 분리되기 때문에 이번 문제에서는 사용 불가능
2.소수판별하는 함수를 따로 만들기
'''
import itertools
import math

numbers = "17"

#소수판별 함수
def find_prime(n):
    if n <= 1:   #n이 0, 1 인 경우
        return False       #False로 가며 함수 종료

    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False    #False로 가며 함수 종료
        return True

#문자열 분리하고 find_prime함수 이용하여 답 구하기
def solution(numbers):
    number = [n for n in numbers]   #문자열 분리

    data = []
    for i in range(1, len(number)+1):   #순열로 모든 경우를 만들기
        data += itertools.permutations(number, i)
    new_number = [int(''.join(p)) for p in data]

    answer = []     #for문 밖에 써줘야 append가 쌓일 수 있음 -> 안에 써주면 매 연산마다 그 연산에 대한 값만 쌓음(즉 한개씩만...)
    for x in new_number:
        if find_prime(x):
            answer.append(x)

    answer = list(set(answer))
    return len(answer)

print(solution(numbers))
