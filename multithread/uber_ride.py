from threading import Lock, Barrier, current_thread


class UberRide:

  def __init__(self):
    self.dc_count = 0
    self.marvel_count = 0
    self.lock = Lock()
    self.barrier = Barrier(4)
    self.ride_count = 0

  def drive(self):
    self.ride_count += 1
    print("Uber ride # {0} on its way".format(self.ride_count))

  def seated(self, group):
    print("{0} {1} seated".format(group, current_thread().getName()))

  def seat_dc(self):
    pass

  def seat_marvel(self):
    pass

