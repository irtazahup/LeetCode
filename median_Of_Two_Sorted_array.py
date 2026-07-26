class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # if nums1[-1] < nums2[0]:
        #     merged_array=nums1+nums2

        #     if len(merged_array)%2==0:
        #        mid = len(merged_array) // 2
        #        left_mid = merged_array[mid - 1]   
        #        right_mid = merged_array[mid]
        #        print(left_mid,right_mid)
        #        median = (right_mid + left_mid) / 2
        #        print(median)  

        #        return median    
        #     else:
        #         return len(merged_array)//2
        
        merged_array=nums1+nums2

        merged_array.sort()
        print(merged_array)
        mid = len(merged_array) // 2
        if len(merged_array)%2==0:
            
            left_mid = merged_array[mid - 1]   
            right_mid = merged_array[mid]
            print(left_mid,right_mid)
            median = (right_mid + left_mid) / 2
            print(median)  
            return median    
        
        return merged_array[mid]