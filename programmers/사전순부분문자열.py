
##################### 통과
def solution(s):
    
    # 문자열에서 가장 큰 문자열과 갯수 찾음 
    # sub_string에 갯수만큼 더해줌 
    # 문자열 = 문자열[가장 큰 문자열의 마지막 인덱스 + 1 : ]  반복
    
    sub_string = ""
    
    while s: 
        biggest_char = max(s)
        biggest_char_count = s.count(biggest_char)
        sub_string += biggest_char_count*biggest_char
        s = s[s.rfind(biggest_char) + 1 : ]
    return sub_string


##################### 효율성 탈락

# 처음에 올 알파벳 탐색 
# 첫자리가 정해지면, 다음 자리 탐색할 문자열은 s[첫자리 알파벳 인덱스 : 끝까지]
# 문자열 없어질 때 까지 반복 

def solution(s):
    sub_string = ""

    while s: 
        biggest_char = ""
        biggest_idx = 0 
        for idx, ele in enumerate(s):
            if ele > biggest_char:
                biggest_char = ele
                biggest_idx = idx
                
        sub_string += biggest_char
        s = s[biggest_idx + 1: ]
    return sub_string

def solution(s):
    sub_string = ""
    while s: 
        biggest_char = max(s)
        max_idx = s.index(biggest_char)
        sub_string += biggest_char
        s = s[max_idx + 1 : ]
    return sub_string


        