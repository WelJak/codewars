def make_readable(seconds):
    sekundy = 0
    minuty = 0
    godziny = 0
    if seconds == 0:
        return "00:00:00"
    else:
        minuty = seconds // 60
        sekundy = seconds - minuty * 60
        if len(str(sekundy)) == 1:
            sekundy = '0' + str(sekundy)
        else:
            sekundy = str(sekundy)
        if minuty >= 60:
            godziny = minuty // 60
            minuty = minuty - godziny * 60
            if len(str(minuty)) == 1:
                minuty = '0' + str(minuty)
            else:
                minuty = str(minuty)
            if len(str(godziny)) == 1:
                godziny = '0' + str(godziny)
            else:
                godziny = str(godziny)
        else:
            if len(str(minuty)) == 1:
                minuty = '0' + str(minuty)
            else:
                minuty = str(minuty)
            godziny = '00'
    return godziny + ':' + minuty + ':' + sekundy
