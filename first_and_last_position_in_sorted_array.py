class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        elif len(nums) == 1 and nums[0] != target:
            return [-1,-1]

        low=0
        high=len(nums)-1

        global_mid=-1

        while low <= high:
            if low == high :
                if nums[low] == target:
                    return [low,low]
                else:
                    return [-1,-1]
            else:
                mid= low + (high-low)/2
             
                if nums[mid]==target:
                   global_mid=mid
                   print(global_mid)
                   break
                    #forward check

                    # if nums[mid+1] == target: 
                    #     return [mid,mid+1]
                    # elif nums[mid-1] == target:
                    #     return [mid-1,mid]
                    # else:
                    #     return [mid,mid]


                if nums[mid] >= target:
                    high=mid
                else:
                    low=mid+1
                    


        if global_mid != -1:

            k=global_mid #forward
            m=global_mid #backward

            while  k < len(nums) and nums[k] == target  :
                k=k+1
            while m > -1 and nums[m] == target:
                m=m-1
            
            return [m+1,k-1]
            

            
            

                
        return [-1,-1]
