#https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1

def array_madness(a,b):
    
    return sum(i**2 for i in a) > sum(j**3 for j in b)
