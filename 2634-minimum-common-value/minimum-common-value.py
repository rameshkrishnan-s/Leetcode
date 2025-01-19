class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m1,m2 = len(nums1),len(nums2)
        p1,p2 = 0,0

        while(p1 < m1 and p2 < m2):
            x = nums1[p1]
            y = nums2[p2]

            if x == y :
                return x
            elif x > y :
                p2+=1
            else:
                p1+=1
        return -1