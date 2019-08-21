def is_square(n): 
    if n>=0:
        x=n**(1/2)
        if x.is_integer():
            return True
        else:
            return False
    else:
        return False
