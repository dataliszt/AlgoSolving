
# 벌집 

target_num = int(input())
init_point = 1 
cnt = 1
while True: 
    if init_point >= target_num:
        break
    init_point += 6 * cnt
    cnt += 1
print(cnt)

    