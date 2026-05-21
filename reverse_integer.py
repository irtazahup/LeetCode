class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative=False
        
         # LeetCode 32-bit integer overflow check
        if x < -2**31 or x > 2**31 - 1:
            return 0
        
        if x < 0:
            x=x*-1
            is_negative=True
        
        temp=0
        while x != 0:
            num=x%10
            temp=(temp*10)+num
            x=x/10
       # Apply the negative sign back
        if is_negative:
            temp = temp * -1
            
       
         # LeetCode 32-bit integer overflow check
        if temp < -2**31 or temp > 2**31 - 1:
            return 0
        
        return temp

        