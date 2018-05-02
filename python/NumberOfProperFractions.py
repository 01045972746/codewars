import math, itertools
def proper_fractions(n):
  p_arr = filter(lambda k: n % k == 0, [int(x) for x in range(2, n)])
  s_arr = []
  for x in p_arr:
    s_arr.append([p for p in range(1, n) if p % x == 0])

  return len(set([x for x in range(1, n)]) - set(list(itertools.chain(*s_arr))))

# print (proper_fractions(1))
# print (proper_fractions(2))
# print (proper_fractions(5))
print (proper_fractions(15))
# print (proper_fractions(25))