"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #just return 0 when nums is empty
        if len(nums) == 0:
            return 0

        #store all start of sequences
        #turn nums into set to get rid of duplicates.
        start_candidates = []
        num_set = set(nums)

        #n is start of a sequence only if there's no number that's less by 1
        for n in num_set:
            if n-1 not in num_set:
                start_candidates.append(n)

        seq_lens = set()
        
        #add lengths of all sequences to a set and return maximum
        for s in start_candidates:
            curr = s
            length = 1
            while curr+1 in num_set:
                length+=1
                curr = curr+1
            seq_lens.add(length)
        
        return max(seq_lens)
