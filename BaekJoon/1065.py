#함수문제_한수
'''
sol
1. n을 입력받는다.
2. 입력받은 n까지의 범위로 반복문을 만들고
3. n의 자리수를 분리해서 list로 집어넣고 각 자리수의 등차수열 이 존재하는지 확인한다.

**문제** 등차수열이 가능한지 확인하는 식을 생각해야함
-> 1~99 까지는 모두 한수이기 때문에 첫번째 if 문에 99까지 따로 분류해주고
100~999는 새로운 if문을 이용해서 한수를 구해준다.

4. 100~999까지중에 조건에 만족하면 cnt += 1 을 한다.
5. 출력

'''
'''N = int(input())

cnt = 0

for i in range(1, N+1):
    if i < 100:     #1~99 까지는 다 한수
        cnt += 1
    else:           #100 부터는  [1][0][0] 을 나눠서 [1][0], [0][0] 비교해서 차가 같으면(등차이면) 한수
        X = list(map(int, str(i)))
        if X[2] - X[1] == X[1] - X[0]:
            cnt += 1
print(cnt)
'''

#함수사용

def func1(result):      #함수이름; func1(result)
    cnt = 0
    for i in range(1, result+1):        #1~result 까지 반복
        if i < 100:
            cnt += 1
        else:
            X = list(map(int, str(i)))
            if X[2] - X[1] == X[1] - X[0]:
                cnt += 1
    return cnt      #return구문 위치 유의할 것, cnt 리턴해줌

result = int(input())       #result에 정수를 input해줌
print(func1(result))