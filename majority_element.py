class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        max_ele=0
        my_dict={}
        for i in nums:
            if i not in my_dict:
                my_dict[i]=1
                if my_dict[i] > max_count:
                    max_ele=i
                    max_count=my_dict[i]
            else:
                my_dict[i]+=1
                if my_dict[i] > max_count:
                    max_ele=i
                    max_count=my_dict[i]

        print(max_count)
        print(max_ele)
        return max_ele      
        
