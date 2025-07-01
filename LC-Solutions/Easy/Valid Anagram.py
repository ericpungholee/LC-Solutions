class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        curr_s = {}
        curr_t = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i not in curr_s:
                curr_s[i] = 1
            else:
                curr_s[i] += 1

        for j in t:
            if j not in curr_s:
                return False
            elif j not in curr_t:
                curr_t[j] = 1
            else:
                curr_t[j] += 1
        print(curr_s)
        print(curr_t)

        if len(curr_s) != len(curr_t):
            return False

        for k in curr_s:
            if curr_s[k] != curr_t[k]:
                return False  
            return True

        