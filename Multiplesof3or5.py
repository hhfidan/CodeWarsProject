def solution(number):
    """
    t = 0
    
    for c in range(number):
        if c%3==0 or c%5==0:
            t+=c
    return t
    """
    #Code begin below
    return sum(c for c in range(number) if c%3==0 or c%5 ==0)
