def solution(num_list):
    if len(num_list) <= 5:
        return []

# 가장 작은 5개의 수를 제외하고 오름차순으로 정렬
    return sorted(num_list[5:], key=int)
print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))