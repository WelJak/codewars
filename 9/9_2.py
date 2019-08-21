def make_readable(seconds):
    sekundy = seconds % 60
    minuty = seconds // 60 % 60
    godziny = seconds // 3600
    return '{:02d}:{:02d}:{:02d}'.format(godziny, minuty, sekundy)
