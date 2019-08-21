def filter_list(l):
    O=[]
    for x in l:
        if not isinstance(x, str):
            O.append(x)
    return O
