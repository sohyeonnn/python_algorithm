#level1_정렬
'''
commands 배열의 길이 만큼 for문
slice
append
'''
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#return = [5, 6, 3]

def solution(array, commands):
    answer = []

    for i in range(len(commands)):  # commands[i][j]  원소만큼

        first = array[commands[i][0] - 1:commands[i][1]]  # slice
        first.sort()  # 배열정렬
        answer.append(first[commands[i][2] - 1])

    return answer

print(solution(array, commands))