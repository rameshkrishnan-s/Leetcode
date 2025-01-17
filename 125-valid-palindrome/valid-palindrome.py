class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = []
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                res.append(s[i])
        
        for i in range(len(res)):
            if res[i] != res[len(res) - i - 1] :
                return False
        return True