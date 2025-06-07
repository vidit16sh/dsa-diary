# find anagram solution !
s = "hello" 
f = "elloh"  
def cout(s):
    char_count = {} 
    for char in s and f:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1 

