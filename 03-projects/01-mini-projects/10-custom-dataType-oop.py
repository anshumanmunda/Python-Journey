class Fraction:
  def __init__(self, x,y):
    self.nume = x
    self.deno = y

  def __str__(self):
      return "{}/{}".format(self.nume, self.deno)

  def __add__(self, other):
    new_nume =   self.nume * other.deno   +  self.deno * other.nume
    new_deno =   self.deno * other.deno   
    return "{}".format(new_nume/new_deno)

  def __sub__(self, other):
    new_nume =   self.nume * other.deno   -  self.deno * other.nume
    new_deno =   self.deno * other.deno   
    return "{}".format(new_nume/new_deno)

  def __mul__(self, other):
    new_nume =  self.nume * other.nume 
    new_deno =  self.deno * other.deno   
    return "{}".format(new_nume/new_deno)
  

  def __truediv__(self, other):
    new_nume =  self.nume * other.deno 
    new_deno =  self.deno * other.nume   
    return "{}".format(new_nume/new_deno)
  
fr1 = Fraction(1,2)
fr2 = Fraction(2,2)

print(f"{fr1} + {fr2} = {fr1 + fr2}")  # Addition  
print(f"{fr1} - {fr2} = {fr1 - fr2}")  # Substraction
print(f"{fr1} * {fr2} = {fr1 * fr2}")  # Multiplaction
print(f"{fr1} / {fr2} = {fr1 / fr2}")  # Division
