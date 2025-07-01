class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = set()
        dups = False
        for n in nums:
            if n not in curr:
                curr.add(n)
            else:
                dups = True
        return dups
