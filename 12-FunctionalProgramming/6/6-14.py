filling = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]
capacity = 500
tolerance = 0.02

def incorrect(capacity,tolerance):
    low = capacity * (1 - tolerance)
    high = capacity * (1 + tolerance)
    return lambda x:x