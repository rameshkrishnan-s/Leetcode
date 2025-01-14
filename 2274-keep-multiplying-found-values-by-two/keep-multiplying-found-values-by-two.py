class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numSet = set(nums)
        while original in numSet :
            original *= 2
        return original