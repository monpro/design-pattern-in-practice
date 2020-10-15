import time
from threading import Condition, Thread


class CountSemaphore:
  def __init__(self, capacity):
    self.capacity = capacity
    self.given = 0
    self.condition_variable = Condition()

  def acquire(self):
    self.condition_variable.acquire()
    while self.given == self.capacity:
      self.condition_variable.wait()
    self.given += 1
    self.condition_variable.notifyAll()
    self.condition_variable.release()

  def release(self):
    self.condition_variable.acquire()
    while self.given == 0:
      self.condition_variable.wait()
    self.given -= 1
    self.condition_variable.notifyAll()
    self.condition_variable.release()


def task1(sem):
  sem.acquire()
  print("acquiring")
  sem.acquire()
  print("acquiring")
  sem.acquire()
  print("acquiring")


def task2(sem):
  sem.release()
  print("releasing")
  sem.release()
  print("releasing")
  sem.release()
  print("releasing")


if __name__ == "__main__":
  semaphore = CountSemaphore(2)
  t1 = Thread(target=task1, args=(semaphore,))
  t2 = Thread(target=task2, args=(semaphore,))
  t1.start()
  time.sleep(1)
  t2.start()

  t1.join()
  t2.join()