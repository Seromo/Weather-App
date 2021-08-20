def convert(t):
    if type(t) not in [int,float]:
        raise TypeError ("The temperature must be a number")
    else:
        new_temp = (t*1.8) + 32 
    return new_temp
    