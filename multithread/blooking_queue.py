import random
import time
from threading import Condition, current_thread, Thread


class BlockingQueue:

  def __init__(self, max_size):
    self.max_size = max_size
    self.cur_size = 0
    self.condition_var = Condition()
    self.queue = []

  def enqueue(self, item):
    self.condition_var.acquire()
    while self.cur_size == self.max_size:
      self.condition_var.wait()

    self.queue.append(item)
    self.cur_size += 1
    self.condition_var.notifyAll()
    self.condition_var.release()

  def dequeue(self):
    self.condition_var.acquire()
    while self.cur_size == 0:
      self.condition_var.wait()

    item = self.queue.pop(0)
    self.cur_size -= 1
    self.condition_var.notifyAll()
    self.condition_var.release()

    return item


def consumerThread(queue):
  while True:
    item = queue.dequeue()
    print("{0} consume item {1}".format(current_thread().getName(), item), flush=True)
    time.sleep(random.randint(1, 3))


def producerThread(queue, val):
  item = val
  while True:
    queue.enqueue(item)
    item += 1
    time.sleep(0.1)


if __name__ == "__main__":
  blockingQueue = BlockingQueue(5)

  consumerThread1 = Thread(target=consumerThread, name="consumer_1", args=(blockingQueue, ), daemon=True)
  consumerThread2 = Thread(target=consumerThread, name="consumer_2", args=(blockingQueue, ), daemon=True)

  producerThread1 = Thread(target=producerThread, name="producer_1", args=(blockingQueue, 100), daemon=True)
  producerThread2 = Thread(target=producerThread, name="producer_2", args=(blockingQueue, 300), daemon=True)

  consumerThread1.start()
  consumerThread2.start()

  producerThread1.start()
  producerThread2.start()

  time.sleep(10)