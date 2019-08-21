def friend(x):
    L=[]
    for person in x:
        if len(person)==4:
            L.append(person)
    return L
