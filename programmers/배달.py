


# 실패
from queue import deque

def solution(N, road, K):
            
    total_time = [0 for x in range(N + 1)]
    next_visit = deque([1])
    while next_visit:
        init = next_visit.popleft()
        for info in road:
            if info[0] > info[1]:
                info[0], info[1]  = info[1], info[0]
                
            if info[0] == init:
                if total_time[info[1]] == 0:
                    total_time[info[1]] += total_time[info[0]] + info[2]
                else:
                    if total_time[info[0]] + info[2] < total_time[info[1]]:
                        total_time[info[1]] = total_time[info[0]] + info[2]
                next_visit.append(info[1])
    return len([x for x in total_time if x > 0 and x <= K]) + 1
    
    
def solution(N, road, K):
    
    
    return 0
