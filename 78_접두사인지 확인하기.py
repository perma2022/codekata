def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string):
        return 0
    
    for i in range(len(is_prefix)):
        if my_string[i] != is_prefix[i]:
            return 0
        
    return 1

print(solution("banana","ban"))
