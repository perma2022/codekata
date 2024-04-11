def solution(arr, n):
    # arr의 길이에 따라 처리하는 방식을 결정합니다.
    if len(arr) % 2 == 1:  # arr의 길이가 홀수인 경우
        for i in range(0, len(arr), 2):  # 모든 짝수 인덱스에 대해
            arr[i] += n  # 해당 인덱스의 값에 n을 더합니다.
    else:  # arr의 길이가 짝수인 경우
        for i in range(1, len(arr), 2):  # 모든 홀수 인덱스에 대해
            arr[i] += n  # 해당 인덱스의 값에 n을 더합니다.
    return arr  # 수정된 배열을 반환합니다.
