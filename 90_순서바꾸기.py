def solution(num_list, n):
    # 새로운 리스트를 생성하기 위해 빈 리스트를 초기화
    new_list = []

    # n+1 번째 원소부터 마지막 원소까지 new_list에 추가
    for i in range(n, len(num_list)):
        new_list.append(num_list[i])

    # 첫 번째 원소부터 n 번째 원소까지 new_list에 추가
    for i in range(n):
        new_list.append(num_list[i])

    return new_list


print(solution([2, 1, 6], 1))
