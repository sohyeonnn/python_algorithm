#팰린드롬수(브1)_문자열, 문자열 인덱싱
'''
-> , <- 방향이 서로 같은 단어인지 확인하면 됨
-> 문자열 역순으로 출력해서 같은 단여면 yes, 아니면 no
'''

while True:
    palindrome = input()

    if palindrome == '0':
        break

    if palindrome == palindrome[::-1]:
        print('yes')
    else:
        print('no')
