class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        nz = 1
        zero_count = 0
        for i in range(len(nums)):
            product*=nums[i]
            if nums[i] != 0:
                nz*=nums[i]
            else:
                zero_count+=1

        
        result = []
        for n in range(len(nums)):
            if zero_count > 1 and nums[n] == 0:
                result.append(product)
            elif nums[n] == 0:
                result.append(nz)
            else:
                result.append(product//nums[n])
        return result
