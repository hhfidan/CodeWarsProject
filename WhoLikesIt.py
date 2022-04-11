def likes(names):
    
    #get the user numbers with len() 
    #do not try to use print, its useless in here.
    
    if (len(names) == 0):
        return "no one likes this"
    elif (len(names) == 1):
        return str(names[0]) + " likes this"
    elif (len(names) == 2):
        return str(names[0]) + " and " +str(names[1]) + " like this" 
    elif (len(names) == 3):
        return str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
    else:
        return str(names[0]) + ", " +str(names[1]) + " and " +str(len(names)-2)+ " others like this"
    
        # First one is done yay yay
              
    pass
