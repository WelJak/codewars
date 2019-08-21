def xo(s):
    counterx=0
    countero=0
    s=s.lower()
    for char in s:
        if char is "x":
            counterx+=1
        elif char is "o":
            countero+=1
    if counterx!=countero:
        return False
    else:
        return True
