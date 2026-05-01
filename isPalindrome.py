# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")

def isPalindrome(s):
    
    i=0
    j=len(s)-1
    is_pal=True
    while i <=len(s)/2 and j >= len(s)/2:
        if s[i]!=s[j]:
            return False
            break
        else:
            i=i+1
            j=j-1
            
     
    return is_pal       

print(isPalindrome('anna'))

        