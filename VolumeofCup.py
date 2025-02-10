import numpy as np

def cup_volume(d1, d2, height):
    r1 = d1/2
    r2 = d2/2
    
    V = (1/3)*(np.pi*height)*(r1**2+r1*r2+r2**2)
    
    return round(V,2)
