def find_it(seq):
    for x in seq:
        count=seq.count(x)
        if count%2==1:
            return x
