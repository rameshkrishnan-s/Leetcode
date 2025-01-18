class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        
        digitSum = 0

        for i in range(len(nums)):
            while(nums[i] > 0):
                digit = nums[i] % 10
                digitSum += digit
                nums[i]//=10
        return abs(sum-digitSum)