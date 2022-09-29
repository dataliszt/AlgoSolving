# 영화감독 숌 

import sys 

n = int(sys.stdin.readline())
tmp = set()
count = 0
string = "666"

while len(tmp) < n:
    
    new_string = str(count) + string
    
    if new_string.count("6666") >= 1:
        start = new_string.index("666")
        tmp_string = new_string[:start] + new_string[start:start + 3]

        for i in range(10**(len(new_string) - len(new_string[:start] + new_string[start:start + 3]))):
            if len(str(i)) + len(tmp_string) != len(new_string):
                remainder = "0" * (len(new_string) - len(tmp_string) - len(str(i))) + str(i)
            else:
                remainder = str(i)
            tmp.add(int(tmp_string + remainder))
    
    tmp.add(int(new_string))
    count += 1
print(sorted(list(tmp))[n - 1])