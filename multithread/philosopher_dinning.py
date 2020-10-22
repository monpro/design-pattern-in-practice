import random
import time
from threading import Semaphore, Thread


class PhilosopherDinning:

  def __init__(self):
    self.forks = [Semaphore(1) for _ in range(5)]
    self.max_dinner = Semaphore(4)

  def life_cycle_philosopher(self, phi_id):
    while True:
      self.contemplate()
      self.eat(phi_id)

  def contemplate(self):
    sleep_time = random.randint(100, 500) / 1000
    time.sleep(sleep_time)

  def eat(self, phi_id):
    # re-entrance lock
    # only 4 philosophers could grab the fork at most
    self.max_dinner.acquire()

    # phi0: need fork 4 and 0
    # phi1: need fork 0 and 1
    # left (phi_id + 4) % 5, right phi_id
    left_fork = phi_id
    right_fork = (phi_id + 4) % 5

    self.forks[left_fork].acquire()
    self.forks[right_fork].acquire()

    print("philosopher {0} is eating".format(phi_id))

    self.forks[left_fork].release()
    self.forks[right_fork].release()

    self.max_dinner.release()


if __name__ == "__main__":
  philosopher_dinning = PhilosopherDinning()
  threads = list()
  for index in range(5):
    threads.append(Thread(target=philosopher_dinning.life_cycle_philosopher, args=(index,)))

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()

