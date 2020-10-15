import random
import time
from threading import Condition, current_thread, Thread


class ReaderWriterLock:

  def __init__(self):
    self.condition_variable = Condition()
    self.writer_working = False
    self.readers = 0

  def acquire_reader_lock(self):
    self.condition_variable.acquire()
    while self.writer_working is True:
      self.condition_variable.wait()
    self.readers += 1
    self.condition_variable.release()

  def release_reader_lock(self):
    self.condition_variable.acquire()
    self.readers -= 1
    if self.readers == 0:
      self.condition_variable.notifyAll()
    self.condition_variable.release()

  def acquire_writer_lock(self):
    self.condition_variable.acquire()
    while self.readers != 0 or self.writer_working is True:
      self.condition_variable.wait()
    self.writer_working = True
    self.condition_variable.release()

  def release_writer_lock(self):
    self.condition_variable.acquire()
    self.writer_working = False
    self.condition_variable.notifyAll()
    self.condition_variable.release()


def writer_thread(lock):
  while True:
    lock.acquire_writer_lock()
    print('{0} writing at {1}, readers={2}'.format(current_thread().getName(),
                                                   time.time(), lock.readers), flush=True)
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
    print('{0} releasing at {1}, readers={2}'.format(current_thread().getName(),
                                                     time.time(), lock.readers), flush=True)
    lock.release_writer_lock()
    time.sleep(1)


def reader_thread(lock):
  while True:
    lock.acquire_reader_lock()
    print('{0} reading at {1}, writer is working={2}'.format(current_thread().getName(),
                                                             time.time(), lock.writer_working), flush=True)
    wait_time = random.randint(1, 2)
    time.sleep(wait_time)
    print('{0} releasing at {1}, writer is working={2}'.format(current_thread().getName(),
                                                             time.time(), lock.writer_working), flush=True)
    lock.release_reader_lock()
    time.sleep(1)


if __name__ == "__main__":
  reader_writer_lock = ReaderWriterLock()
  writer_thread_1 = Thread(target=writer_thread, args=(reader_writer_lock,), name="writer_thread_1", daemon=True)
  writer_thread_2 = Thread(target=writer_thread, args=(reader_writer_lock,), name="writer_thread_2", daemon=True)
  readers = []
  writer_thread_1.start()
  for i in range(3):
    readers.append(Thread(target=reader_thread, args=(reader_writer_lock,), name="reader_thread_{0}".format(i + 1), daemon=True))

  for thread in readers:
    thread.start()
  writer_thread_2.start()
  time.sleep(15)