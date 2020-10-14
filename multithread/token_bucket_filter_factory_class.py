import time
from threading import Condition, Thread, current_thread


class TokenBucketFilterFactory:

  @staticmethod
  def getTokenBucketFilter(capacity):
    token_bucket_instance = MultiThreadTokenBucketFilter(capacity)
    token_bucket_instance.init()
    return token_bucket_instance


class MultiThreadTokenBucketFilter:

  def __init__(self, max_token):
    self.max_token = max_token
    self.possible_tokens = 0
    self.condition_variable = Condition()

  def init(self):
    daemon_thread = Thread(target=self.daemonThread)
    daemon_thread.setDaemon(True)
    daemon_thread.start()

  def daemonThread(self):
    while True:
      self.condition_variable.acquire()
      if self.possible_tokens < self.max_token:
        self.possible_tokens += 1
      self.condition_variable.notify()
      self.condition_variable.release()

      time.sleep(1)

  def get_token(self):
    self.condition_variable.acquire()
    while self.possible_tokens == 0:
      self.condition_variable.wait()
    self.possible_tokens -= 1
    self.condition_variable.release()

    print("giving token to thread {0} at {1}".format(current_thread().getName(), int(time.time())))


if __name__ == "__main__":
  token_bucket_filter = TokenBucketFilterFactory.getTokenBucketFilter(1)
  threads = []
  for i in range(10):
    threads.append(Thread(target=token_bucket_filter.get_token))

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()