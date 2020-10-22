import random
import time
from threading import Semaphore


class PhilosopherDinning:

  def __init__(self):
    self.forks = [Semaphore(1) for _ in range(5)]

  def life_cycle_philosopher(self, phi_id):
    while True:
      self.contemplate()
      self.eat(phi_id)

  def contemplate(self):
    sleep_time = random.randint(100, 500) / 1000
    time.sleep(sleep_time)

  def eat(self, phi_id):
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