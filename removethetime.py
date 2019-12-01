def shorten_to_date(long_date):
    sep = ','
    no_time = long_date.split(sep, 1)[0]
    return no_time