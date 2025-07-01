class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val_key = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in val_key:
                val_key[sorted_word].append(word)
            else:
                val_key[sorted_word] = [word]
        return list(val_key.values())