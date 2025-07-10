class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c = {}
        res = 0
        l, maxf = 0, 0

        for r in range(len(s)):
            c[s[r]] = 1 + c.get(s[r], 0)
            maxf = max(maxf, c[s[r]])

            while (r-l+1) - maxf > k:
                c[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
        
