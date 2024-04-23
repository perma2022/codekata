def solution(names):
    group_names = []

    for i in range(0, len(names), 5):
        group_names.append(names[i])

    return group_names


def solution(names):
    return names[::5]
