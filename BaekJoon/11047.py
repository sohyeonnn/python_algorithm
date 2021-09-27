#greedy/ 동전0(실2)

n, k = map(int, input().split())

dongjeon = []
count = 0


for i in range(n):
    dong_n = int(input())
    dongjeon.append(dong_n)

dongjeon.sort(reverse=True)

for j in dongjeon:
    count += k // j     #count값에 k를 동전으로 나눈 몫을 더해준다. (1. 4200//1000 -> 4가 더해진다.)
    k = k % j           #k는 동전으로 나눈 나머지값으로 계속 반복한다. (2. 4200%1000 -> 200, 200원으로 for문 다시반복)

print(count)            #for문을 돌고난 count값을 출력한다.