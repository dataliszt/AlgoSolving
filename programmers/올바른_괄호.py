

# 테스트 케이스 2개 탈락
def solution(s):
    if s[0] == ")" or s[-1] == "(" or len(s) <= 1:
        return False
    count = 0
    for ele in s:
        if ele == "(":
            count += 1
        else:
            count -= 1
    return count == 0


# refactoring

def solution(s):
    count = 0
    for ele in s:
        if ele == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0