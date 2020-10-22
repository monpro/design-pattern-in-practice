from threading import Condition, current_thread


class Barrier(object):
  def __init__(self, size):
    self.barrier_size = size
    self.reached_thread = 0
    self.released_thread = 0
    self.condition_variable = Condition()

  def reached(self):
    self.condition_variable.acquire()
    self.reached_thread += 1

    # block any new threads from proceeding until all the threads
    # have reached the previous Barrier having been released
    while self.reached_thread == self.barrier_size:
      self.condition_variable.wait()

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
