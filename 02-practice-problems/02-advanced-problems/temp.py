class Vehicle:
  def __init__(self, capacity: int) -> None:
    self.total_capacity = capacity
    self.fare = 100 * capacity 

  def fare(self):
    print(f'Total cost for {self.total_capacity} passangers = {self.fare}')

class Bus(Vehicle):
  pass

Obj = Vehicle()
