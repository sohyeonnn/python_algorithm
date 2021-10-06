#덩치(실버5)_브루트포스

n =int(input())

info_list = []
#rank = []

#빈 리스트에 kg, cm 변수를 저장
for i in range(n):
    kg, cm = map(int, input().split())
    info_list.append((kg, cm))

#덩치 비교
for i in range(n):

    #기본 순위는 1위로 고정, 2중for문에서 나머지 값들과 비교하여 자신보다 큰 덩치가 있다면 count 증가
    count = 1   #1에서 시작하면 마지막에 1씩 안더해줘도됨(k의 덩치 순위는 k+1이라서 +1을 해줘야하기때문)
    for j in range(n):

        # 몸무게와 키 모두 자신보다 큰 사람을 센다.
        #몸무게와 키 두 값이 전부 큰 경우에만 -> 큰 덩치로 판단하기 때문에 만약 두 값 다 크다면
        if (info_list[i][0] < info_list[j][0]) and (info_list[i][1] < info_list[j][1]):
            count += 1      #count + 1 해준다.
    #rank.append(count)


#for i in rank:
    print(count, end=' ')