# Closure For Python 2
def running_average():
  arr = []
  def abc(n):
      arr.append(n)
      return round(float(sum(arr)) / float(len(arr)), 2)
  return abc

# For Python 3
def running_average_for3():
  arr = []
  def abc(n):
      arr.append(n)
      return round(sum(arr) / len(arr), 2)
  return abc


r_avg = running_average()
print r_avg(10)
print r_avg(11)
print r_avg(12)