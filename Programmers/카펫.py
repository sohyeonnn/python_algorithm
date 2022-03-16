#level2_완탐/구현
'''
갈색 수 + 노랑 수-> 가로 * 세로(격자 전체값) 값이 나옴
=> 격자 전체값이 나오는 경우의 수를 모두 구한 뒤 가로가 더 큰 수인 경우만 남긴다.

*point
가로길이가 더 길다
*간단하게 생각하기
가로길이 = a, 세로길이 = b 일때
**문제풀이 핵심 식
brown = 2a + 2b - 4 (각각의 변을 더한 다음, 중복되는 모서리 부분 4개를 빼준다)
yellow = ab - brown
ab = brown + yellow

-> 해당 문제는 a, b 를 구해야함
'''
brown = 10
yellow = 2


def solution(brown, yellow):
    answer = []
    total = brown + yellow      #전체 타일 개수 = 갈 + 노

    for length in range(1, total+1):    #total = 12 일 때, 1~12까지 length의 값을 확인해주기 위해 이처럼 range를 설정한다. -> 약수 확인을 위한 식
        if (total/length) % 1 == 0:     #전체 타일을 length로 나눈 나머지 값이 0이라면
            width = int(total/length)   #width는 total을 해당 length로 나눈 값이다 (약수끼리 짝임 ex. 2, 6 / 3, 4 ...)

            if width >= length:     #가로 길이가 세로 길이보다 크면서
                if 2*width + 2*length == brown +4:  #해당 조건을 만족하는 가로, 세로 값을 answer로 return한다.
                    return [width,length]

    return answer


print(solution(brown, yellow))