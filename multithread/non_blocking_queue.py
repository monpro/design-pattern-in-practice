import random
import time
from threading import current_thread, Thread, Lock


class NonBlockingQueue:

  def __init__(self, max_size):
    self.max_size = max_size
    self.queue = []
    self.lock = Lock()

  def enqueue(self, item):
    with self.lock:
      cur_size = len(self.queue)
      if cur_size == self.max_size:
        return False
      else:
        self.queue.append(item)
        return True

  def dequeue(self):
    with self.lock:
      cur_size = len(self.queue)

      if cur_size != 0:
        return self.queue.pop(0)

      else:
        return False


def consumerThread(queue):
  while True:
    item = queue.dequeue()
    if not item:
      print("{0} can't dequeue an item".format(current_thread().getName()), flush=True)
    else:
      print("{0} consume item {1}".format(current_thread().getName(), item), flush=True)
    time.sleep(random.randint(1, 3))


def producerThread(queue, val):
  item = val
  while True:
    flag = queue.enqueue(item)
    if flag:
      print("{0} produce item {1}".format(current_thread().getName(), item), flush=True)
      item += 1
      time.sleep(0.1)


if __name__ == "__main__":
  blockingQueue = NonBlockingQueue(5)

  consumerThread1 = Thread(target=consumerThread, name="consumer_1", args=(blockingQueue, ), daemon=True)
  consumerThread2 = Thread(target=consumerThread, name="consumer_2", args=(blockingQueue, ), daemon=True)

  producerThread1 = Thread(target=producerThread, name="producer_1", args=(blockingQueue, 100), daemon=True)
  producerThread2 = Thread(target=producerThread, name="producer_2", args=(blockingQueue, 300), daemon=True)

  consumerThread1.start()
  consumerThread2.start()

  producerThread1.start()
  producerThread2.start()

  time.sleep(10)