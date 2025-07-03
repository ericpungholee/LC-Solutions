class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [c for c in s.lower() if c.isalnum()]

        if len(s) == 0 or len(s) == 1:
            return True
        
        l = 0
        r = len(s)-1

        valid = False

        while l < r:
            if s[l] == s[r]:
                valid = True
            else:
                return False
            l+=1
            r-=1
        
        return valid
        
