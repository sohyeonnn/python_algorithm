#level1_완탐
'''
수포자들의 찍는 방식을 list로 만들고
answers 의 값을 하나씩 비교하여 일치하는 값이 있으면...

*point
A, B, C 패턴보다 answers가 길게 들어오는 경우를 고려해줘야함
%(나머지)연산을 통해  -> A[i % len(A)] 로 바꿔주어 해결한다.
'''

answers = [1, 3, 2, 4, 2]

def solution(answers):
    # 수포자들의 찍는 규칙
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_count = [0 for i in range(3)]  # A, B, C 답 개수를 저장해줄 리스트-> 0으로 설정해서 답을 맞추면 +1을 해준다.

    res = []
    for i in range(len(answers)):  # answers = [1,2 ,3 ,4, 5] 인 경우
        ans = answers[i]  # answers[0] = 1 = ans
        if A[i % len(A)] == ans:
            answer_count[0] += 1
        if B[i % len(B)] == ans:
            answer_count[1] += 1
        if C[i % len(C)] == ans:
            answer_count[2] += 1


    m = max(answer_count)
    for i, v in enumerate(answer_count):
        if m == v:
            res.append(i+1)

    return res

print(solution(answers))

print(2%5)