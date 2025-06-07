class Solution(object):
    def productExceptSelf(self, nums):        
        p, z_c = 1, 0

        for n in nums:
            if n == 0:
                z_c += 1
            else:
                p *= n
        if z_c > 1:
            return [0] * len(nums)
        if z_c == 1:
            return [p if n == 0 else 0 for n in nums]
        else:
            return [p/n for n in nums] 
