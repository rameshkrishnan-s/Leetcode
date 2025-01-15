class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()
        nums = sorted(nums)
        l = 0 
        r = len(nums)-1

        while(l < r):
            avg = (nums[l]+nums[r])/2 

            if avg not in res :
                res.add(avg)
            l+=1
            r-=1
        return len(res)
        