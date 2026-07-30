class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1

        max_water=0

        while left < right:
            min_height=min(height[left],height[right])
            current_water=min_height*(right-left)
            max_water=max(max_water,current_water)
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        
        return max_water