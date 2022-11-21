# 2xn 타일링 
import sys 

n = int(sys.stdin.readline())

def solution(n):
    table = [0 for x in range(n + 1)]
    for i in range(len(table)):
        if i < 4:
            table[i] = i
        else:
            table[i] = table[i - 1] + table[i - 2]
    print(table)
    return table[-1] % 10007 

if __name__ == "__main__":
    print(solution(9))