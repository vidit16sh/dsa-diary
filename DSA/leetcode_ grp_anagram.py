# grp anagram problem!
strs =  ["eat","tea","tan","ate","nat","bat"]
d = {}
for i in strs: 
    key = ''.join(sorted(i)) 
    if key not in d: 
        d[key] = [] 
    d[key].append(i) 
print(d.values())