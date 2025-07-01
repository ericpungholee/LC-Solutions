class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        start_candidates = []
        num_set = set(nums)

        for n in num_set:
            if n-1 not in num_set:
                start_candidates.append(n)

        seq_lens = set()

        for s in start_candidates:
            seq = [s]
            curr = s
            for n in num_set:
                if curr+1 in num_set:
                    curr = curr+1
                    seq.append(curr)
            seq_lens.add(len(seq))
        
        return max(seq_lens)
            