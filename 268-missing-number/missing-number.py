class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0
        sum = 0
        total = 0
        for i in range(len(nums)):
            sum += nums[i]
            total += i+1
            res = total - sum
        return res