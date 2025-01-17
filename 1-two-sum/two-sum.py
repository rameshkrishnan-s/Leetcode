class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)

        for i in range(n):
            mp[nums[i]]  = i
        
        for i in range(n):
            complement = target - nums[i]

            if complement in mp and mp[complement] != i :
                return [i,mp[complement]]
            mp[nums[i]] = i
        return []