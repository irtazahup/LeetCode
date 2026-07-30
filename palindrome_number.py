class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        sample=''
        current=x
        if x == 0:
            return True
        while current > 0: 
            temp=current%10
            sample=sample+str(temp)
            current=current/10
        print(sample)
       
        if str(x) == sample:
            return True
        else :
            return False