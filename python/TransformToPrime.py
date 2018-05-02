import math
def minimum_number(numbers):
  s = sum(numbers)
  n = s
  if s == 3 or s == 2 or s == 1:
    return 0

  if is_Prime(s):
    return 0
  else:
    while True:
      n += 1
      if is_Prime(n):
        break
    
    return n-s

def is_Prime(number):
  for i in range(2, int(math.sqrt(number)) + 1):
    if not number % i:
      return False
  return True

print minimum_number([3, 1, 2])
print minimum_number([5, 2])
print minimum_number([1, 1, 1])
print minimum_number([2,12,8,4,6])
print minimum_number([50,39,49,6,17,28])
