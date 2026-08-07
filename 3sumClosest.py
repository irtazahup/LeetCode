class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        # min_diff=float('inf')
        
        nums.sort()
        print(nums)
        closest_sum=float('inf')
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

            while left < right :
                inner_sum=nums[i]+nums[left]+nums[right]

                if abs(target-inner_sum) < abs(target-closest_sum):
                    closest_sum=inner_sum
                
                if inner_sum < target:
                    left=left+1
                else:
                    right=right-1

        return closest_sum