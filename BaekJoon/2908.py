#상수(브2)

'''
slice
- slice를 이용해서 string을 뒤집을 수 있다.
- [start:stop:step]순으로 입력
- [::-1]    = 역순
'''

number1, number2 = input().split()


reverse_number1 = number1[::-1]
reverse_number2 = number2[::-1]

if reverse_number1 > reverse_number2:
    print(reverse_number1)
else:
    print(reverse_number2)