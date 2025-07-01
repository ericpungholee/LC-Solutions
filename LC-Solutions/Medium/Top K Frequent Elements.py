class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        values = []
        for key, value in count.items():
            values.append(value)
        
        sorted_values = sorted(values)
        result = []
        for key, value in count.items():
            if value in sorted_values[-k:]:
                result.append(key)
        
        return result




        
            
