# 카드 2

import sys 
from queue import deque

### 시간초과
card_list = [x for x in range(1, int(sys.stdin.readline()) + 1)]
while True:
    if len(card_list) == 1:
        print(card_list[0])
        break 
    del card_list[0]
    card_list.append(card_list[0])
    del card_list[0]
    
### 정답 : deque 자료구조
card_list = deque([x for x in range(1, int(sys.stdin.readline()) + 1)])
while True:
    if len(card_list) == 1:
        print(card_list[0])
        break
    card_list.popleft()
    card_list.append(card_list.popleft())
    
### 어떻게 이런 공식을 유도?
a = int(input())
b = 2
while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break