class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] in h:
                l = max(h[s[r]]+1, l)
            h[s[r]] = r
            res = max(res, r-l+1)
        return res
        
