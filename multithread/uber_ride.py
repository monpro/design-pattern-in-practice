import random
from threading import Lock, Barrier, current_thread, Semaphore, Thread


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
    print("{0} {1} seated\n".format(group, current_thread().getName()))

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
      ride_leader = True
    else:
      self.lock.release()
      self.marvel_waiting.acquire()

    self.seated("marvel")
    self.barrier.wait()

    if ride_leader is True:
      self.drive()
      self.lock.release()


def controller_simulation():
  uber_ride = UberRide()
  dc = 10
  marvel = 10

  total = dc + marvel
  print("Total {0} dc and {1} marvel".format(dc, marvel))

  riders = list()
  while total != 0:
    flag = random.randint(0, 1)
    if flag == 0 and dc > 0:
      riders.append(Thread(target=uber_ride.seat_dc))
      dc -= 1
      total -= 1
    elif flag == 1 and marvel > 0:
      riders.append(Thread(target=uber_ride.seat_marvel))
      marvel -= 1
      total -= 1

  for rider in riders:
    rider.start()

  for rider in riders:
    rider.join()

def random_simulation():
  uber_ride = UberRide()
  dc = 0
  marvel = 0
  riders = list()
  for _ in range(16):
    flag = random.randint(0, 1)
    if flag == 0:
      riders.append(Thread(target=uber_ride.seat_dc))
      dc += 1
    elif flag == 1:
      riders.append(Thread(target=uber_ride.seat_marvel))
      marvel += 1
  print("Total {0} dc and {1} marvel".format(dc, marvel))

  for rider in riders:
    rider.start()

  for rider in riders:
    rider.join()


if __name__ == "__main__":
  controller_simulation()
  # random_simulation()