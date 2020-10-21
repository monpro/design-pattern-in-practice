from threading import Lock, Barrier, current_thread, Semaphore


class UberRide:

  def __init__(self):
    self.dc_count = 0
    self.dc_waiting = Semaphore(0)
    self.marvel_count = 0
    self.marvel_waiting = Semaphore(0)
    self.lock = Lock()
    self.barrier = Barrier(4)
    self.ride_count = 0

  def drive(self):
    self.ride_count += 1
    print("Uber ride # {0} on its way".format(self.ride_count))

  def seated(self, group):
    print("{0} {1} seated".format(group, current_thread().getName()))

  def seat_dc(self):
    ride_leader = False

    self.lock.acquire()
    self.dc_count += 1

    if self.dc_count == 4:
      self.dc_waiting.release()
      self.dc_waiting.release()
      self.dc_waiting.release()

      self.dc_count -= 4
      ride_leader = True
    elif self.dc_count == 2 and self.marvel_count >= 2:
      self.dc_waiting.release()
      self.marvel_waiting.release()
      self.marvel_waiting.release()

      self.dc_count -= 2
      self.marvel_count -= 2
      ride_leader = True
    else:
      self.lock.release()
      self.dc_waiting.acquire()

    self.seated("dc")
    self.barrier.wait()

    if ride_leader is True:
      self.drive()
      self.lock.release()

  def seat_marvel(self):
    ride_leader = False
    self.lock.acquire()
    self.marvel_count += 1
    if self.marvel_count == 4:
      self.marvel_waiting.release()
      self.marvel_waiting.release()
      self.marvel_waiting.release()

      self.marvel_count -= 4
      ride_leader = True
    elif self.marvel_count == 2 and self.dc_count >= 2:
      self.marvel_waiting.release()
      self.dc_waiting.release()
      self.dc_waiting.release()

      self.marvel_count -= 2
      self.dc_count -= 2
    else:
      self.lock.release()
      self.marvel_waiting.acquire()

    self.seated("marvel")
    self.barrier.wait()

    if ride_leader is True:
      self.drive()
      self.lock.release()

