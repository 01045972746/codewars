# -*- coding: utf-8 -*-
from itertools import cycle
def thirt(n):
  k, kt = 0, 0
  while True:
    kt = k
    pool = cycle([1, 10 , 9, 12, 3, 4])
    arr = [int(x) for x in list(str(n))] if not k else [int(x) for x in list(str(k))]
    k = sum(map(lambda x: x[0] * x[1], zip(reversed(arr), pool)))

    if kt == k:
      return k

thirt(1234567)

