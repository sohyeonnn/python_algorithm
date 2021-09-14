#문자열 반복
'''

'''

t = int(input())

for i in range(t):
    r, s = input().split()

    for num in s:
        result = num * int(r)
        print(result, end='')
    print()
