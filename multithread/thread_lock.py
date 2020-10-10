import time
from threading import Lock, current_thread, Thread

shareState = [1, 2, 3]
listLock = Lock()


def thread_a_operation():
  listLock.acquire()
  print("{0} has acquired the lock".format(current_thread().getName()))
  time.sleep(3)
  shareState[0] = 12
  print("{0} about to release the lock".format(current_thread().getName()))
  listLock.release()
  print("{0} has released the lock".format(current_thread().getName()))


def thread_b_operation():
  listLock.acquire()
  print("{0} has acquired the lock".format(current_thread().getName()))
  print(shareState[0])
  print("{0} about to release the lock".format(current_thread().getName()))
  listLock.release()
  print("{0} has released the lock".format(current_thread().getName()))


if __name__ == "__main__":
  thread_a = Thread(target=thread_a_operation(), name='thread_a')
  thread_a.start()

  thread_b = Thread(target=thread_b_operation(), name='thread_b')
  thread_b.start()

  thread_a.join()
  thread_b.join()