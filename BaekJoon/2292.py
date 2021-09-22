#벌집(브2)
'''
벌집
- 규칙성; 1 6 12 18 24 ...
=> 벌집의 개수가 6의 배수로 증가
=> 첫 번째를 제외하고선 6의 배수로 나아간다.

- 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
=> 벌집은 6배수로 증가
'''

n = int(input())

room = 1            #벌집의 개수, 1부터 시작
result_room = 1

while n > room:
    room += 6 * result_room     #벌집이 6의 배수로 증가하낟.
    result_room += 1            #while문을 반복하는 횟수를 뜻함함print(result_room)
print(result_room)

