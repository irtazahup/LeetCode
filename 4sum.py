class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]
       
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left=j+1
                right=len(nums)-1
                while left < len(nums) and right < len(nums) and left < right :
                    inner_sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if inner_sum == target :
                        if [nums[i],nums[j],nums[left],nums[right]] in output:
                            left=left+1
                            right=right-1
                        else:    
                            output.append([nums[i],nums[j],nums[left],nums[right]])
                            left=left+1
                            right=right-1
                    elif inner_sum < target:
                        left=left+1
                    else:
                        right=right-1
        
       
        return output














