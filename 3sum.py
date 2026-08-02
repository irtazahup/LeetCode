class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        output=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 if [nums[i] , nums[j] , nums[k]] in output:
        #                     continue
        #                 output.append([nums[i] , nums[j] , nums[k]])

        # print(output)
        # return output
      
   
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left < right :
               
                if nums[i] + nums [left] + nums[right]> 0:
                    right=right-1
                elif  nums[i] + nums [left] + nums[right]<0:
                    left=left+1
                else:
                    if [nums[i] , nums[left] , nums[right]] in output:
                        left=left+1
                        right=right-1
                        continue
                    output.append([nums[i] , nums[left] , nums[right]])
                    left=left+1
                    right=right-1
              
        
        print(output)
        return output

