import re
def kebabize(string):
    return ''.join(['-'+x.lower() if x.isupper() and idx != 0 else x.lower() for idx, x in enumerate(re.sub('[^a-zA-Z]', '', string))])



# Clever
# def kebabize(s):
#     return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')