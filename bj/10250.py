# ACM 호텔 

"""
- 첫째줄 테스트 케이스 갯수 
- H, w, N 
"""

# 처음 답 
case_count = int(input())
for i in range(case_count):
    H, W, N = map(int, input().split())
    new_h = N % H
    new_w = N // H + 1

    if new_h == 0:
        new_h = H
        new_w -= 1 
        
    str_h = str(new_h)
    str_w = str(new_w)
    
    if len(str_w) < 2:
        str_w = "0" + str_w
    print(str_h + str_w)


# 리팩토링 답
case_count = int(input())
for i in range(case_count):
    H, W, N = map(int, input().split())
    new_h = N % H
    new_w = N // H + 1

    if new_h == 0:
        new_h = H
        new_w  = N // H
    print(f"{new_h * 100 + new_w}")
    