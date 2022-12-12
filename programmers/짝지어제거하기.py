
def solution(s):
    # 알파벳 비교를 위한 리스트
    former_list = [] 
    
    for ele in s:
        # 만약 리스트가 비어있지 않고, 마지막 인덱스와 ele가 같다면, pop
        # 아니면 append 
        if len(former_list) != 0 and former_list[-1] == ele:
            former_list.pop()
        else:
            former_list.append(ele)
    if former_list:
        return 0
    return 1

################### runtime error 
def solution(s):
    
    string_list = list(s)
    i, j = 0, 1
    while string_list:
        if j == len(s):
            return 0
        
        if string_list[i] == string_list[j]:
            for _ in range(2):
                string_list.pop(i)
            if i != 0 and j != 1:
                i -= 1
                j -= 1
        else:
            i += 1
            j += 1
    return 1

def solution(s):
    while s:
        duplicated = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                duplicated += 1
                break 
        if duplicated == 0:
            return 0 
        else:
            left, right = s[:i], s[i + 1 + 1:]
            s = left + right
    return 1