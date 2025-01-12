class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for num in nums :
            if num not in mp : 
                mp[num] = 1
            else:
                mp[num]+=1
        
        for num, count in mp.items() :
            if count > 1 :
                return True
        return False