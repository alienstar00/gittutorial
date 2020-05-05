def delete_starting_evens(lst):
    for k in range(0,len(lst)): 
        if lst[0]%2 == 0:  
            lst.remove(lst[0])
        else:
            break
    return lst
    return bobby_is_final



def delete_starting_evens_while(lst):
    length = len(lst)
    while(length>0 and lst[0]%2 == 0):                                
        lst.remove(lst[0])
        length -= 1
    return lst
        


    
print("using for loop",delete_starting_evens([8, 4,10, 11, 12, 15]))
print("using for loop",delete_starting_evens([10, 8, 4]))
print("using while loop",delete_starting_evens_while([8,4,10,11,12,15]))
print("using while loop",delete_starting_evens_while([10,8,4]))