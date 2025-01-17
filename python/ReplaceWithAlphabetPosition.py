import string, re
def alphabet_position(text):
    alpha = dict((x, idx+1) for idx, x in enumerate(string.ascii_lowercase))
    return ' '.join([str(alpha[x]) for x in re.sub('[^a-zA-Z]', '', text.lower())])


alphabet_position("The sunset sets at twelve o' clock.")
# "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"