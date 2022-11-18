# 단어공부 

# 막코딩 
string = input().lower()
char_dict = {}
top_number = 0
top_char = ""
duplicated = 0
for char in string:
    if char_dict.get(char) is None:
        char_dict[char] = 1
    else:
        char_dict[char] += 1

for key, value in char_dict.items():
    if value > top_number:
        top_number = value 
        top_char = key
        duplicated = 0
    elif value == top_number:
        duplicated += 1
    else:
        pass 
    
if duplicated > 1:
    print("?")
else:
    print(top_char.upper())
        
        
# refactoring 
from collections import defaultdict

string = input().lower()
char_dict = defaultdict(int)
duplicated = 0
max_value = 0
top_char = ""
for char in string:
    char_dict[char] += 1

for value in char_dict.values():
    max_value = max(max_value, value)

for key, value in char_dict.items():
    if value == max_value:
        duplicated += 1 
        top_char = key 
if duplicated > 1:
    print("?")
else:
    print(top_char.upper)
    
# other's solution 
words = input().upper()
unique_words = list(set(words))

cnt_list = []

for i in unique_words:
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
