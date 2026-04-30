def count_frequency(s):
    
    my_dict={}
    
    for i in s:
        if i not in my_dict:
            my_dict[i]=1
        else:
            my_dict[i]+=1
    
    return my_dict

print(count_frequency('aabbcc'))