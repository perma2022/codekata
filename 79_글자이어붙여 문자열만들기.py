def solution(my_string, index_list):
    result = ""
    for index in index_list:
        result += my_string[index]
    return result

    
print(solution("cvsgiorszzzmrpaqpe",[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))