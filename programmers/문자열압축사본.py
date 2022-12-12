def solution(string):
    
    shortest_len = len(string)
    
    # 분할 갯수를 1부터 문자열 길이까지 나눠가며 탐색 
    for i in range(1, (len(string) // 2) + 1):

        q_string = string  # 분할 갯수만큼 pop 하기 위해. queue의 방식으로 원본 string을 복사
        former_list = []   # 분할 갯수 count list 
        merge_string = ""   # 탐색 끝나면, 문자열 생성
        
        # q_string에서 문자열이 없어질 때까지 반복 
        while q_string:   
            
            # 만약 현재 문자가 former_list에 없으면 count 1 
            # 존재한다면 former_list[-1][1]에 접근하여 갯수 update 
            cur = q_string[:i]
            if not former_list:
                former_list.append([cur, 1])
            else:
                if cur == former_list[-1][0]:
                    former_list[-1][1] += 1
                else:
                    former_list.append([cur, 1])
                    
            q_string = q_string[i:]
            
        # q_string 탐색이 끝난 후, 해당 문자열 조합 
        for (ele, num) in former_list:
            merge_string += (ele if num == 1 else f"{num}{ele}")
        
        # 매 분할갯수 마다 길이 저장
        shortest_len = min(shortest_len, len(merge_string))
        
    return shortest_len

## 실패 
def solution(string):
    shortest_len = len(string)
    for i in range(1, len(string) - 1):
        temp_string = ""
        cnt = 1
        for j in range(0, len(string) - 1, i):
            cur, next = string[j : j + i], string[j + i : j + (i * 2)]
            if cur == next:
                cnt += 1
                if j == len(string) - 2:
                    temp_string += f"{cnt}{cur}"
            else:
                if cnt > 1:
                    temp_string += f"{cnt}{cur}"
                else: 
                    temp_string += cur
                    
                cnt = 1
        shortest_len = min(shortest_len, len(temp_string))
    return shortest_len

    