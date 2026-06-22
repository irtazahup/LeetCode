class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        length=len(s)

        d_list = [[0] for _ in range(numRows)]
        print(d_list)

        i=0
        output=''
        row=0
        direction=True
        while i < length :

            if row !=numRows:

                while row < numRows and i < length:
                    
                    d_list[row].append(s[i])
                    i=i+1
                    row=row+1

            else:
                row=numRows-2
                
                while row > -1 and i < length:
                    print(row)
                    d_list[row].append(s[i])
                    i=i+1
                    row=row-1
                row=1

        
        for row_n in d_list:
            for j in row_n:
                if j==0:
                    continue
                else:
                    output=output+j
        print(output)
        return output

































            # if direction == True:

            #     if row <= numRows and row >= 1:
            #         d_list[row].append(s[i])
            #         print(d_list,row)
            #         i=i+1
            #         row=row+1
            #     else:
            #         direction=False
            #         row=numRows-2

            # else:
            #     if row <= numRows and row >=1:
            #         d_list[row].append(s[i])
            #         i=i+1
            #         row=row-1
            #     else:
            #         direction=True
            #         row=1
        
        


