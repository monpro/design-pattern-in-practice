import time
from threading import Thread, Semaphore


class AsyncExecutor:

  def work(self, callback):
    time.sleep(5)
    callback()

  def execute(self, callback):
    Thread(target=self.work, args=(callback,)).start()


class SyncExecutor(AsyncExecutor):

  def __init__(self):
    self.sem = Semaphore(0)

  def work(self, callback):
    super().work(callback)
    self.sem.release()

  def execute(self, callback):
    super().execute(callback)
    self.sem.acquire()


def test_task():
  print('task done')


if __name__ == "__main__":
  # executor = AsyncExecutor()
  executor = SyncExecutor()
  executor.execute(test_task)
  print("main threading exiting")