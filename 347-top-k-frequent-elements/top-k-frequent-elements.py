class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}
        res = []
        for num in nums :
            if num not in mp :
                mp[num] = 1
            else :
                mp[num] += 1
        
        for num in sorted(mp,key = lambda x : mp[x], reverse=True):
            res.append(num)
            k-=1
            if k == 0:
                break
        return res