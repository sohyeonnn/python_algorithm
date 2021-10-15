import sys

n = int(sys.stdin.readline().rstrip())


def hanoi(n, start, fin, other):#원반개수, 출발지기둥번호, 목적지기둥번호, 나머지기둥번호

    if n < 2:       #n=1은 어차피 바로 이동
        print(start, fin)
        return

    hanoi(n-1, start, other, fin)
    print(start, fin)
    hanoi(n-1, other, fin, start)

print((2**n)-1)     #총이동수

hanoi(n, 1, 3, 2)
