def removeDuplicates(s):
    empty_list=[]
    for i in s:
        if i not in empty_list:
            empty_list.append(i)
        
    return empty_list

print(removeDuplicates([1,1,2,2,3,3]))
    