import random
import time
from concurrent.futures import Future
from threading import current_thread, Thread, Lock


class NonBlockingQueue:

  def __init__(self, max_size):
    self.max_size = max_size
    self.queue = []
    self.queue_waiting_puts = []
    self.queue_waiting_gets = []
    self.lock = Lock()

  def enqueue(self, item):
    future = None
    with self.lock:
      cur_size = len(self.queue)
      if cur_size == self.max_size:
        future = Future()
        self.queue_waiting_puts.append(future)
      else:
        self.queue.append(item)
        if len(self.queue_waiting_gets) != 0:
          future_get = self.queue_waiting_gets.pop()
          future_get.set_result(True)
      return future

  def dequeue(self):
    result = None
    future = None
    with self.lock:
      cur_size = len(self.queue)

      if cur_size != 0:
        result = self.queue.pop()

        if len(self.queue_waiting_puts) > 0:
          self.queue_waiting_puts.pop().set_result(True)
      else:
        future = Future()
        self.queue_waiting_gets.append(future)
    return result, future


def consumerThread(queue):
  while True:
    item, future = queue.dequeue()
    if not item:
      print("{0} received a future".format(current_thread().getName()), flush=True)
    else:
      print("{0} consume item {1}".format(current_thread().getName(), item), flush=True)
    time.sleep(random.randint(1, 3))


def producerThread(queue, val):
  item = val
  while True:
    future = queue.enqueue(item)
    if future is not None:
      while not future.done():
        print("{0} waiting for future to be resolved".format(current_thread().getName()), flush=True)

        time.sleep(0.1)
    else:
      print("{0} produce item {1}".format(current_thread().getName(), item), flush=True)
      item += 1


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