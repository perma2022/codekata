def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer += my_string[i][parts[i][0]:parts[i][1]+1]

    return = answer


# for i in range(len(my_strings)):: 이 부분은 반복문으로, my_strings 리스트의 각 요소를 처리하기 위해 사용됩니다. range(len(my_strings))는 0부터 my_strings 리스트의 길이까지의 숫자를 생성합니다.
# answer += ...: answer 변수에 값을 누적하는 연산자입니다. 여기서는 각 문자열의 부분 문자열을 answer에 더해줍니다.
# my_string[i]: 이 부분은 my_strings 리스트의 i번째 요소를 의미합니다. 반복문을 통해 각 요소에 접근할 때 사용됩니다.
# [parts[i][0]:parts[i][1]+1]: 이는 슬라이싱 구문으로, 현재 문자열의 부분 문자열을 추출합니다. parts[i][0]은 부분 문자열의 시작 인덱스를, parts[i][1]은 끝 인덱스를 나타냅니다. +1을 더하는 이유는 슬라이스의 끝 인덱스를 포함하기 위해서입니다.
# 이 코드는 my_strings 리스트의 각 요소에서 해당하는 부분 문자열을 추출하여 answer에 더하는 작업을 반복합니다.
