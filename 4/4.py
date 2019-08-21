def maskify(cc):
    aa=''
    for x in range(0, len(cc)-4):
        aa+='#'
    return aa+cc[-4:]
