class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        el = 0
        count = 0

        for i in range(len(nums)):
            if count == 0 :
                count = 1
                el = nums[i]
            elif el == nums[i] :
                count +=1
            else:
                count -=1

        return el