def solution(my_string,is_suffix):
    
    # 문자열의 끝에서부터 길이를 역으로 계산합니다. 
    # 예를 들어, is_suffix의 길이가 3이라면, 
    # -len(is_suffix)는 -3이 되며, 
    # 이는 my_string의 끝에서부터 3개 문자를 의미합니다.
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    else: 
        return 0
    
print(solution("banana", "ana"))