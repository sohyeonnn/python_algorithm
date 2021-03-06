#회의실배정(실2)_그리디알고리즘
'''
*
1)빨리 끝나는 회의 순서대로 정렬해야함.
=> 빨리 끝날수록 뒤에서 고려해볼 회의가 많아지기 때문에...
2)끝나는 시간이 같을 경우
=> 빨리 시작하는 순서대로 정렬해야함

***(1step)끝나는 시간의 오름차순 ->(2step)시작하는 시간의 오름차순으로 정렬해줘야함
'''

#예전풀이
import sys
'''
n = int(sys.stdin.readline().rstrip())

time = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))

time.sort()
time.sort(key=lambda x:x[1])

'''

'''
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

이렇게도 가능
'''

'''
room = 1
end_time = time[0][1]

#range(1,n)
for i in range(1, n):
    if time[i][0] >= end_time:
        room += 1
        end_time = time[i][1]
print(room)
'''


#다시플기
#끝나는시간의 내림차순으로 정렬하면 되지않을까?
n = int(sys.stdin.readline().rstrip())

time = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))

#2번째 인자(key)에 대해 reverse sort
time.sort(key=lambda x:x[1], reverse=True)

room = 1
end_time = time[0][1]

#range(1,n)
for i in range(1, n):
    if time[i][0] >= end_time:
        room += 1
        end_time = time[i][1]
print(room)
