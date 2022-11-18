
# Hashing 
string_len = int(input())
string = input()

r = 31 
M  = 1234567891

hash_dict = {}
hashed_value = 0

for i in range(97, 97 + 26):
    hash_dict[chr(i)] = i % 97 + 1
    
for idx, char in enumerate(string): 
    hashed_value += (hash_dict[char] * (r**idx))
print(hashed_value % M)


# refactoring
string_len = int(input())
string = input()

r = 31 
M  = 1234567891

hashed_value = 0 
for i in range(string_len):
    hashed_value += (ord(string[i]) % 97 + 1) * r**i
print(hashed_value % M)