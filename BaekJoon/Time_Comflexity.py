#0x00시간, 공간복잡도; 문제1
'''
def func1(N):
    cnt = 0
    for i in range(1, N+1):     #for문에서 i가 1부텉 N까지 돌면서 3으로 나누어지는 지 5로 나누어지는지 확인한다 => 따라서 시간복잡도는 O(N)이다.
        if i%3 == 0 or i%5 == 0:
            cnt += i
    return cnt
N = int(input())
print(func1(N))
'''


#0x00시간, 공간복잡도; 문제2
'''
def func2(K, N):
    for i in range(N):
        for j in K:
            if K[j] + K[i] == 100:     #내부 원소의 합잉 100이면... 어떻게 쓰지?
                cnt = 1
            else:
                cnt = 0
    return cnt


N = int(input())
for i in range(N):
    K = list(map(int, input().split()))
print(func2(K, N))
'''


#0x00시간, 공간복잡도; 문제3
'''
def func3(N):
    for i in range(N):
        i += 1
        if i*i == N:
            result = 1
            break
        else:
            result = 0
    return result

N = int(input())
print(func3(N))
'''


#0x00시간, 공간복잡도; 문제4
#???.....
def func4(N):
    result = 0
    for i in range(N):
        i += 1
        result = max(2**i)
N = int(input())
print(func4(N))

#몰라.....뭔가 공부방식이 잘못된듯