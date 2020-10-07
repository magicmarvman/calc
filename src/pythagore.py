from math import sqrt

def hypotenuse(a, b):
  return sqrt(a**2 + b**2)

def pythagore(a, b, c):
  a = int(a)
  b = int(b)
  c = int(c)
  return(a**2 + b**2 == c**2)
