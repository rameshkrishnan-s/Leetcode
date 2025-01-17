class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        res = 0
        if x < 0 :
            x = x * -1
        while x > 0 :
            digit = x % 10

            if res > (2**31)//10 or res < -(2**31)//10:
                return 0

            res = res * 10 + digit
            x //= 10
        return res * -1 if temp < 0 else res 