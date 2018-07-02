def series_sum(n):
    if not n:
        return format(n, '.2f')
    return_n = 1.0
    for x in range(1, n):
        return_n += 1/(x*3+1)

    return format(round(return_n,2) , '.2f')

# Clever
'''
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
'''
