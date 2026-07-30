class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        
        output=''
        if len(s) == 1:
            return s

        while left < len(s):
            for r in range(left+1,len(s)+1):
                temp=s[left:r]
                if temp == temp[::-1]:
                    if len(temp) > len(output):
                        output=temp
            left=left+1
        
        print(output)

        return output

        