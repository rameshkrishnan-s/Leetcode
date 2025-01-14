class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = 0
        maxIndex = 0

        for i in range(len(nums)):

            if maxNum < nums[i]:
                maxNum = nums[i]
                maxIndex = i
        temp = maxIndex
        for i in range(len(nums)):
            if i != temp :
                if maxNum < 2*nums[i]:
                    maxIndex = -1
                    break
                else:
                    maxIndex = temp
        return maxIndex
