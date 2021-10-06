#회의실배정(실2)_그리디알고리즘
'''
*
1)빨리 끝나는 회의 순서대로 정렬해야함.
=> 빨리 끝날수록 뒤에서 고려해볼 회의가 많아지기 때문에...
2)끝나는 시간이 같을 경우
=> 빨리 시작하는 순서대로 정렬해야함

***(1step)끝나는 시간의 오름차순 ->(2step)시작하는 시간의 오름차순으로 정렬해줘야함
'''
n = int(input())

time = []

for i in range(n):
    s, e = map(int, input().split())
    time.append((s, e))

time.sort()
time.sort(key=lambda x:x[1])

'''
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

이렇게도 가능
'''
room = 1
end_time = time[0][1]
for i in range(n):
    if time[i][0] >= end_time:
        room += 1
        end_time = time[i][1]
print(room)
