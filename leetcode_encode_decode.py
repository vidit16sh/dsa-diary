"""
Question:  
Encode and Decode Strings (Leetcode-style)

Design an algorithm to encode a list of strings into a single string, and then decode that string back to the original list.

---

Approach: Custom Delimiter Encoding

**Encoding Strategy:**
- For each string, prefix it with its length followed by a delimiter (e.g., `$`).
- Example: `"neet"` becomes `"4$neet"`.
- Concatenate all such encodings into a single string.

**Decoding Strategy:**
- Iterate through the encoded string.
- For each substring:
  - Read the digits before `$` to get the length of the string.
  - Extract that many characters after the `$`.
  - Repeat until the full string is decoded.

Why this works:
- The `$` acts as a unique delimiter separating the length and actual content.
- Using the length ensures we handle any characters, including `$`, inside the actual string itself.

Time Complexity:
- Encoding: O(N), where N is the total number of characters in all strings.
- Decoding: O(N), same as above.

Test Case:
Input: ["neet", "code", "love", "you"]  
Encoded: "4$neet4$code4$love3$you"  
Decoded Output: ["neet", "code", "love", "you"]
"""

def encode(strs): 
    f = ""
    for k in strs:  
        f += str(len(k)) + '$' + k 
    return f

def decode(s): 
    fstr = [] 
    i = 0 
    while i < len(s): 
        j = i
        while s[j] != '$':            # find the delimiter
            j += 1
        l = int(s[i:j])               # extract length of next string
        i = j + 1                     # move past '$'
        fstr.append(s[i:i+l])        # extract the actual string
        i += l                       # move to next encoded segment
    return fstr

# ----------------------------
# 🧪 Test Run
# ----------------------------
input = ["neet", "code", "love", "you"]
t = encode(input)
print("Encoded string:", t)           # Output: "4$neet4$code4$love3$you"
print("Decoded list:", decode(t))     # Output: ["neet", "code", "love", "you"]
