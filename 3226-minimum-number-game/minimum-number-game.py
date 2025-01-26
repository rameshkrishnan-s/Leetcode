class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = 1
        r = len(nums)

        while l < r :
            nums[l] , nums[l-1] = nums[l-1] , nums[l]
            l+=2
        return nums