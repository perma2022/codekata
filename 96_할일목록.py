def solution(todo_list, finished):
    unfinished = []

    for i in range(len(todo_list)):
        if not finished[i]:
            unfinished.append(todo_list[i])

    return unfinished


def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer


def solution(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]
