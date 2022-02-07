'''
주어진 수 중 3개의 수를 더해서 소수가 되는 경우의 개수를 구하는 문제

[ 풀이방법 ]
- 소수판별알고리즘 작성 해야함
- combinations를 이용해 중복을 제거한 3개의 숫자 조합을 만들어주고 각각을 더해서 소수판별알고리즘 이용해서 answer 출력
'''
from itertools import combinations

nums = [" 프로그래머스 입력값"]

#소수판별 알고리즘(2이상의 자연수에 대해)
def is_prime_number(x):
    #2부터 x-1까지의 모든 수를 확인하면서
    for i in range(2, x):
        #x가 해당 수로 나누어 떨어진다면, 약수가 있는 것이므로
        if x % i == 0:
            #소수가 아님
            return False
    #그렇지 않다면 소수가 맞음
    return True


def solution(nums):
    answer = 0
    # combinations이용해서 원소 3개로 구성된 리스트 생성
    arr = list(combinations(nums, 3))
    for a, b, c in arr:
        if is_prime_number(a+b+c):
            answer += 1
    return answer