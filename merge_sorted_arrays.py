class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # start=m

        # j=0
        # while start < m+n:
        #     nums1[start]=nums2[j]
        #     j=j+1
        #     start=start+1
        
        # print(nums1)
        # return nums1.sort()


        i=0
        j=0

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] <= nums2[j] and nums1[i]!=0:
                
        #         i=i+1
        #     elif nums1[i] > nums2[j]:
        #         nums1[i] ,nums2[j]=nums2[j] ,nums1[i]
        #         i=i+1
        #     elif nums1[i] == 0:
        #         print("this block should exploid")
        #         nums1[i] = nums2[j]
        #         del nums2[j]
        # print(nums2)
        # print(nums1)
        # return nums1
        