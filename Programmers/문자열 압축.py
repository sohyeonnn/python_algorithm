#문자열 압축
'''
*point
1. 처음엔 하나씩 쪼개고, 두개씩, 세개씩 쪼개는 형식으로 for문을 돌린다.
2. 그 중 길이가 제일 작은 값을 return한다.
'''

s = 'aabbccaabbcc'
#s = 'xababcdcdababcdcd'


def solution(s):
    answer = len(s)     #문자열의 길이 -> 7

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):      #s
        print("step:",step)
        compressed = ""
        print(compressed)
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        print("prev:",prev)
        count = 1

        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):

            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1

            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 다시 초기화
                count = 1

        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev

        # 만들어지는 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer

print(solution(s))


'''
5/26 재풀이


def solution(s):
    answer = len(s)     #아무리 커봤자 문자열 본래의 길이이기 때문에 len(s)

    #압축할 단위 설정(절반이 최대 -> 압출하면 줄어드는게 반보다 넘게 줄어들수가 없으니까)
    for i in range(1, len(s)//2+1):

        res = ''    #최종 압축문자열
        cnt = 1
        tmp = s[:i]     #현재단위문자열(단위문자열 초기화)

        #i개씩 문자열을 가른다. i개씩 증가하는 for문을 돌면서, j부터 i+j까지 (문자열 길이가 i이라고 쳣을 때) 문자열을 슬라이싱한다.
        for j in range(i, len(s)+i, i):

            if tmp == s[j:j+i]:     #s[j:j+i] 는 다음문자열부터 자를 단위문자열만큼 슬라이싱한 값. 즉 다음 단위문자열을 뜻함/ tmp와 s[j:j+i]가 같은지 비교하면 개수를 셀 수 있다.

                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1
        answer = min(answer, len(res))
    return answer
'''