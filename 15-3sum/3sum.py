class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start,end = i+1 , len(nums)-1

            while start < end :

                if nums[start] + nums[end] + nums[i] == 0:
                    res.append([nums[start],nums[end],nums[i]])
                    start+=1
                    while nums[start] == nums[start-1] and start < end :
                        start+=1
                elif nums[start] + nums[end] + nums[i] > 0 :
                    end -=1
                else:
                    start+=1
        return res