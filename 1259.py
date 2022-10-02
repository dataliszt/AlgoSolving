# 팰린드롬수 

import sys 

while True:
    num_string = sys.stdin.readline().strip()
    
    if num_string == "0":
        break
    
    elif num_string == num_string[::-1]:
        print("yes")
    else:
        print("no")