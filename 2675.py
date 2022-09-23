# 문자열 반복 

case_count = int(input())
for i in range(case_count):
    repeat_num, string = input().split()
    repeat_num = int(repeat_num)
    new_string = ""
    for char in string:
        new_string += char * repeat_num
    print(new_string)