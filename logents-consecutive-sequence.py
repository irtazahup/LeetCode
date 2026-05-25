class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        length=1
        list_len=[0]
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if nums[i] - nums[i-1] == 1:
                length=length+1
            else:
                list_len.append(length)
                length=1
                
    
        
        if length > max(list_len):
            return length
        return max(list_len)
       