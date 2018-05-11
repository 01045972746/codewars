def zeroes(base, number):
  factors = factor(base)
  result = []
  for x in factors.keys():
    count, i = 0, x
    while i <= number:
      count += number / i
      i *= x
    result.append(count / factors[x])
  return min(result)

def factor(base):
  d = 2
  dic = {}
  while d <= base:
    c = 0
    while base % d == 0:
      c += 1
      base /= d
    if c != 0:
      dic[d] = c
    d += 1
  return dic

print(zeroes(60, 7753))