class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = []
        for i in words:
            ans.append(i[0])
        
        return ''.join(ans) == s