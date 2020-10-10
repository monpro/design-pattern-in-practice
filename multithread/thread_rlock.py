from threading import RLock, Thread

rLock = RLock()


def child_task():
  rLock.acquire()
  print("child task executing")
  rLock.release()


def release_task():
  rLock.release()
  print("rLock released")
  rLock.release()


rLock.acquire()
rLock.acquire()

rLock.release()
# uncomment the following code
# re-entrant lock can only be released by same thread
# rLock.release()


# thread = Thread(target=child_task)
thread = Thread(target=release_task)
thread.start()
thread.join()
