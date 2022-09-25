# 분해합 

number = map(int, input().split())
c_list = []
for i in range(number - 54, number):
    temp_num = i
    constructor = temp_num
    for char in str(temp_num):
        temp_num += int(char)
    if temp_num == number:
        c_list.append(constructor)
if len(c_list) == 0:
    print(0)
else:
    print(c_list[0])