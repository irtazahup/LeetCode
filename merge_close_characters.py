class Solution(object):
    def mergeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i=0
      
        while i < len(s):
            j=i+1
            while j <= i+k and j < len(s):
                if s[i] == s[j] :
                    new_s = s[:j] + s[j+1:]
                    s=new_s
                    i=0
                    continue 
                j=j+1
            i=i+1
        print(s)

        return s
        











