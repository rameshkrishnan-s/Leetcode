class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = {}

        for num in arr:
            if num not in mp :
                mp[num] = 1
            else:
                mp[num] +=1

        if len(set(mp.values())) != len(set(arr)):
            return False
        return True