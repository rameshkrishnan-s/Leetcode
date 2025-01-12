class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0 
        end = x
        res = 0
        while(start <= end):
            mid = (start + end)//2
            if mid * mid == x :
                return mid
            elif(mid*mid > x):
                end = mid - 1
            elif mid*mid < x:
                start = mid + 1
                res = mid
            
        return res