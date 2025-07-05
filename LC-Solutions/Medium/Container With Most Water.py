class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            h = min(height[l], height[r])
            a = (r - l) * h
            max_area = max(max_area, a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

        
