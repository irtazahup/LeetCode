class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        output=0
        is_negative=False

        # for i in s:
        #     if i == ' ':
        #         continue
        #     if output == -1 and i == '0':
        #         continue
            
        #     if i == '-' and output==-1:
        #         is_negative=True
        #         continue
        #     if i not in ['1','2','3','4','5','6','7','8','9']:
                
        #         break
        #     # if i not in ['1','2','3','4','5','6','7','8','9'] and output==0:
        #     #     break
        #     if output == -1:
        #         output=0
        #     temp=int(i)
        #     output=(output*10)+temp
        # print(output)
        # if is_negative:
        #     return output*-1
        # if output == -1:
        #     return 0
        # return output
        if s == '':
            return 0
        i=0
        while i < len(s) and s[i] == ' ':
            i=i+1
        if i == len(s):
            return 0
        if s[i] == '-':
            is_negative=True
            i=i+1
        elif s[i] == '+':
            is_negative=False
            i=i+1
        
        
        while   i <len(s) and s[i] in ['0','1','2','3','4','5','6','7','8','9']:
            temp=int(s[i])
            output=(output*10)+temp
            i=i+1

        print(output)

        if is_negative:
            output=output*-1
            
        if output > (2**31) - 1:
            output = (2**31) - 1
        elif output < -2**31:
            output = -2**31

        return output
