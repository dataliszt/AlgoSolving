# 설탕 배달 
import sys 
#N = int(sys.stdin.readline().strip())

def count_bag(N):
    temp_list = []
    if N % 5 == 0:
        return N // 5
    if N % 3 == 0:
        temp_list.append(N // 3)
        
    temp = 0
    while True:
        N -= 5
        temp += 1
        if N % 3 == 0:
            temp += N // 3
            temp_list.append(temp)
            break
        if N < 0:
            count = -1
            temp_list.append(count)
            break 
    
    # if len(temp_list) > 1 and -1 in temp_list:
    #     return max(temp_list)
    # elif len(temp_list) > 1 and -1 not in temp_list:
    #     return min(temp_list)
    # elif len(temp_list) == 1 and -1 not in temp_list:
    #     return temp_list[0]
    # else:
    #     return -1
    if len(temp_list) == 2 and -1 not in temp_list:
        return min(temp_list)
    else:
        return max(temp_list)
    
if __name__ == "__main__":
    for N in [18, 4, 6, 9, 11]:
        print(count_bag(N))

