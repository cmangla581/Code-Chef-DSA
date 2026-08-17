
# We have to find the minimum number of operations 

class Solution: 
    def count_nnon_minimum(self, nums): 

        if not nums: 
            return 0 

        minimum = min(nums) 
        count_min = nums.count(minimum)  

        return len(nums) - count_min 

