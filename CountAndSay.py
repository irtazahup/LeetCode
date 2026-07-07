class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # if n == 1 :
        #     return "1"
        
        # else:
        #     base_rle=self.countAndSay(n-1)
        #     output=''
        #     i=0
        #     while i < len(base_rle):
        #         count=0
        #         j=i+1
        #         while j < len(base_rle):
        #             if base_rle[j]==base_rle[i]:
        #                 count=count+1
        #                 j=j+1
        #                 print(count)
        #             else:
        #                 if count==0:
        #                     count=count+1
        #                 output=output+str(count)+base_rle[i]

        #                 i=j+1
        #                 print(output,i)
        #     return output
        if n == 1:
            return '1'
        
        start=3
        output='11'
        while start <= n:
            
            if start==1:
                output='1'
            
            else:
                temp_output=output
                # if len(temp_output) == 1:
                #     output='11'
                #     continue
                    
                j=0
                count=1
                base_output=''
                while j < len(temp_output):
                   
                    i=j+1
                    print(j,i,start)
                    while  i < len(temp_output) and temp_output[i] == temp_output[j]:
                        count=count+1
                        i=i+1
                    base_output=base_output+str(count)+temp_output[j]
                    
                    j=i
                    count=1
                    
                output=base_output
               
            start=start+1
        return output


                        
                



