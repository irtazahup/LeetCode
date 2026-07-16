class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOdd=0
        sumEven=0
       
        if n == 1:
            return 1
        while n > 0:
            sumOdd=sumOdd+(2*n-1)
            sumEven=sumEven+(2*n)
           
            n=n-1
       
     

        reminder=float('inf')
        divisor=sumOdd
        current=sumEven
        
        while reminder != 0 :
            reminder=current%divisor
            current=divisor
            if reminder!=0:
                divisor=reminder

        return divisor