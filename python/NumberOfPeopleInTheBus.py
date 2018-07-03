def number(bus_stops):
    return sum([x if idx % 2 == 0 else -x for idx, x in enumerate(reduce(lambda x, y: x+y, bus_stops))])

# Clever
'''
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
'''
