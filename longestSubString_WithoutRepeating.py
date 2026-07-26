class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left=0
        max_len=1

        # for right in range(1,len(s)):
        #     if s[right] in s[left:right]:
        #         left=left+1
        #         # right=right-1
        #         print(left,right)
        #     else:
        #         max_len=max(max_len,right-left+1)
        
        right=1
        if not s:
            return 0
        while right < len(s):
            if right==left:
                right=right+1
            elif s[right] in s[left:right]:
                left=left+1
            else:
                max_len=max(max_len,right-left+1)
                right=right+1



        return max_len