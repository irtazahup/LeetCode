class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
    
        
        is_negative=False
        if x < 0 :
            is_negative=True
            x=x*-1
        
        reversed_num=0

        while x != 0:
            reminder=x%10
            print(x)
            x=x/10
            reversed_num=(reversed_num*10)+reminder
           
        
        print(reversed_num)
        if reversed_num < -2**31 or reversed_num > (2**31)-1:
            return 0
        if is_negative:
            return -1*(reversed_num)
        return reversed_num  
        
        