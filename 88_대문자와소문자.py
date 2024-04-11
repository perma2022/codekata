def solution(my_string):
    result = ""  # 변환된 문자열을 저장할 빈 문자열을 초기화합니다.
    for char in my_string:  # 문자열의 각 문자에 대해 반복합니다.
        if char.isupper():  # 문자가 대문자인 경우
            result += char.lower()  # 소문자로 변환하여 결과 문자열에 추가합니다.
        elif char.islower():  # 문자가 소문자인 경우
            result += char.upper()  # 대문자로 변환하여 결과 문자열에 추가합니다.
        else:
            result += char  # 대소문자가 아닌 경우(숫자, 특수 문자 등) 변환 없이 추가합니다.
    return result  # 변환된 문자열을 반환합니다.
