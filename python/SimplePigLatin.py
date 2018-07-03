import re
def pig_it(text):
    return ' '.join([ x[1:] + x[0:1] + 'ay' if re.match(r'^\w+$', x) else x for x in text.split() ])

# Clever
'''
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''
