# 분해합 

number = int(input())
if number < len(str(number)) * 9:
    init_number = 1
else: 
    init_number = number - len(str(number)) * 9 

c_list = [] 
for i in range(init_number, number):
    temp_num = i 
    constructor = i 
    for char in str(temp_num):
        temp_num += int(char)
    if temp_num == number:
        c_list.append(constructor)
if len(c_list) == 0:
    print(0)
else:
    print(sorted(c_list)[0])