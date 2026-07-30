class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==1:
            return strs[0]
        min_length = min(len(w) for w in strs)

        output=""

        i=0
        j=0
        current=""
        is_pre=False
        while j < min_length:
            for i in range(len(strs)):
                if i == 0:
                    current=strs[i][j]
                else:
                    if current == strs[i][j]:
                       is_pre=True
                    else:
                      
                        is_pre=False
                        break
            if is_pre:
                output=output+current
                current=""
            else:
                break
            j=j+1
       
        return output

