class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low=0
        high=len(nums)-1

        while low <= high:

            mid=low+((high-low)//2)
            # print(mid,low,high)

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                print(mid)
                low=mid+1
                print(low)
               

            if nums[mid] > target:
                high=mid-1
        
        return low
        