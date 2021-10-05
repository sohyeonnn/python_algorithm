#분해합(브2)

n = int(input())

result = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))      #str함수를 이용해 i의 각 자리수를 a 리스트에 넣어줌
    result = i + sum(a)             #기존 입력 n과 자리수 분리된 a의 합을 더해준다.
    if result == n:                 #생성자가 있다면
        print(i)
        break
    elif i == n:                    #생성자가 없다면
        print(0)