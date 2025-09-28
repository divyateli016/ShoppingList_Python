def splitAt(remainder:str,separator:str):
    find_pos = remainder.find(separator)
    if find_pos==-1:#this returns -1 on failure means not found
        result = remainder
        return result,""
    else:
        finalresult = remainder[0:find_pos]
        remainder = remainder[find_pos+1:]#in python we do not have the reference operator which will be modified by the caller function hence this line 
        #only assigns to the local variable hence we will return both remainder and the result in the function like below
        #while calling we will take to arguments like part,remainder = splitAt(remainder,separator)
        return finalresult,remainder