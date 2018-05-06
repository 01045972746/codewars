def find(seq):
    d = (max(seq) - min(seq)) / len(seq)
    return (len(seq)+1) * (2*min(seq) + (len(seq))*d) / 2 - sum(seq)

find([3, 9, 1, 11, 13, 5])