# 🧩 Question:
# Given a string `s`, partition it into as many parts as possible 
# so that each letter appears in at most one part, and return a list 
# of integers representing the size of these parts.
# (This is similar to the Leetcode problem "Partition Labels")

# ✅ Greedy Approach:
# - First, record the last index of each character in the string.
# - Then, iterate through the string and expand the current partition
#   to the farthest last occurrence of characters seen so far.
# - When the current index reaches the end of the current partition,
#   we can split and start a new partition.

# 🔍 Test Case:
# Input: s = "xyxxyzbzbbisl"
# Output: [10, 1, 2]  -> Explanation:
# - "xyxxyzbzbb" → all characters x, y, z, b occur within this range.
# - "i" → isolated
# - "sl" → s and l do not appear after this

s = "xyxxyzbzbbisl"
dic = {}

# Step 1: Record the last index of each character
for i, x in enumerate(s): 
    dic[x] = i  # store latest (rightmost) index of each character

output = [] 
lp = 0  # left pointer to mark the start of current partition

# Step 2: Traverse and decide partitions
for i, x in enumerate(s): 
    if i == 0: 
        size = dic[x]  # initialize size with first char's last index
    if size == 0: 
        size = dic[x]  # handle reset after partition
    if i < size and dic[x] > size: 
        size = dic[x]  # extend size if current char appears later
    if i == size:      # reached end of current partition
        output.append(size + 1 - lp)  # add partition size
        lp = size + 1  # move left pointer to start next partition
        size = 0       # reset size for next partition

print(output)
