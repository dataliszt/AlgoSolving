# 설탕 배달 
import sys 
#N = int(sys.stdin.readline().strip())

def count_bag(N):
    temp_list = []
    if N % 5 == 0:
        return N // 5
    if N % 3 == 0:
        temp_list.append(N // 3)
    if True:
        new_N = N
        temp = 0
        while True:
            new_N -= 5
            if new_N < 0:
                break 
            temp += 1
            if new_N % 3 == 0:
                temp += new_N // 3
                temp_list.append(temp)
                break
    if True:
        new_N = N
        temp = 0
        while True:
            new_N -= 3
            if new_N < 0:
                break 
            temp += 1
            if new_N % 5 == 0:
                temp += new_N // 5
                temp_list.append(temp)
                break
    if len(temp_list) == 0:
        return -1 
    return min(temp_list)

# refactoring 

def count_bag(N):
    count = 0
    while True:
        if N % 5 == 0:
            count += N // 5 
            break
        N -= 3
        if N < 0:
            break 
        count += 1
    if N < 0:
        return -1 
    return count 

    
if __name__ == "__main__":
    for N in [4998]:
        print(count_bag(N))

