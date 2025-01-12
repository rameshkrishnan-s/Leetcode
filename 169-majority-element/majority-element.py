class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mp = {}

        for num in nums :
            if num not in mp :
                mp[num] = 1
            else:
                mp[num] += 1
        
        max = len(nums)//2
        for num , count in mp.items() :
            if count > max :
                return num
        