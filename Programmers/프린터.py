'''
완전탐색
'''

def solution(priorities, location):

    answer = 0   #반복 회수
    while len(priorities):     #prio1rities길이가 0이 아닌 동안
        for i in range(len(priorities)):    #리스트를 처음부터 확인
            if priorities[i] == max(priorities):  #리스트에서 가장 큰 값과 현재 값이 같다면
                answer += 1     #프린트 한 것으로 간주하고 1을 더해준다
                priorities[i] = 0   #프린트된 값은 0으로 바꿔준다
                if i == location:   #만약 location과 i가 일치한다면
                    return answer   #답을 반환한다