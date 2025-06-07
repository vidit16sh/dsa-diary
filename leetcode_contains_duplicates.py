#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 
# eg : [1,2,3] return false , [1,2,3,3] return true, 
class Solution(object): 
    def __init__(self):
        pass
    def containsDuplicate(self, nums): 
        return len(nums) != len(set(nums)) # it Returns true if the len(nums) is not equal to len(unique nums) else False 

s1 = Solution() 
print(s1.containsDuplicate([2,14,18,22,22]))