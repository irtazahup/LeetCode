class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                return [digits[0]+1]
        number=0
        for i in digits:
            number=number*10+i
        
        number=number+1
        new_digits=[]

        while number!=0:
            new_digits.append(number%10)
            number=number//10
        
        return new_digits[::-1]


obj = Solution()
print(obj.plusOne([9,9,9]))