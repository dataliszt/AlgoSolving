# 체스판 다시 칠하기 

import sys 
#### string 결합
n, m = map(int, sys.stdin.readline().strip().split())
w, b = "W", "B"
string = ''
for i in range(n):
    string += sys.stdin.readline()
string_list = string.strip().split()

#### 슬라이딩 윈도우로 탐색
row, col = 0, 0 
last_string_head = ""
cnt_list = []

while True: 
    if col + 8 > m: 
        col = 0 
        row += 1
        
    if row + 8 > n:
        break 

    for char in [b, w]:
        cnt = 0 
        for i, string in enumerate(string_list[row : row + 8]): # row 
            string = string[col : col + 8] # col
            if i == 0: 
                if char == b:
                    cnt += string[::2].count(w)
                    cnt += string[1::2].count(b)
                    last_string_head = b
                else:
                    cnt += string[::2].count(b)
                    cnt += string[1::2].count(w)
                    last_string_head = w
            else: 
                if last_string_head == b:
                    cnt += string[::2].count(b)
                    cnt += string[1::2].count(w)
                    last_string_head = w
                else:
                    cnt += string[::2].count(w)
                    cnt += string[1::2].count(b)
                    last_string_head = b
        cnt_list.append(cnt)
    col += 1
print(min(cnt_list))
