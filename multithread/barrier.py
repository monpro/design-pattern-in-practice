import time
from threading import Condition, current_thread, Thread


class Barrier(object):
  def __init__(self, size):
    self.barrier_size = size
    self.reached_thread = 0
    self.released_thread = 0
    self.condition_variable = Condition()

  def reached(self):
    self.condition_variable.acquire()

    # block any new threads from proceeding until all the threads
    # have reached the previous Barrier having been released
    while self.reached_thread == self.barrier_size:
      self.condition_variable.wait()

    self.reached_thread += 1

    if self.reached_thread == self.barrier_size:
      self.released_thread = self.barrier_size
    else:
      while self.reached_thread < self.barrier_size:
        self.condition_variable.wait()

    self.released_thread -= 1

    if self.released_thread == 0:
      self.reached_thread = 0

    print("{0} released".format(current_thread().getName()))
    self.condition_variable.notifyAll()
    self.condition_variable.release()


def simulate_thread(barrier_instance, sleep_time):
  time.sleep(sleep_time)
  print("Thread {0} reached the barrier".format(current_thread().getName()))
  barrier_instance.reached()
  time.sleep(sleep_time)
  print("Thread {0} reached the barrier".format(current_thread().getName()))
  barrier_instance.reached()
  time.sleep(sleep_time)
  print("Thread {0} reached the barrier".format(current_thread().getName()))
  barrier_instance.reached()


if __name__ == "__main__":
  barrier = Barrier(3)

  t1 = Thread(target=simulate_thread, args=(barrier, 0.5))
  t2 = Thread(target=simulate_thread, args=(barrier, 1))
  t3 = Thread(target=simulate_thread, args=(barrier, 1.5))

  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()