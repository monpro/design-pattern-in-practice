import time
from threading import Lock, current_thread, Thread


class TokenBucketFilter:

  def __init__(self, max_token):
    self.max_token = max_token
    self.last_request_item = time.time()
    self.possible_tokens = 0
    self.lock = Lock()

  def get_token(self):
    with self.lock:
      self.possible_tokens = int(time.time() - self.last_request_item)
      if self.possible_tokens > self.max_token:
        self.possible_tokens = self.max_token

      if self.possible_tokens == 0:
        time.sleep(1)
      else:
        self.possible_tokens -= 1

      self.last_request_item = time.time()
      print("giving token to thread {0} at {1}".format(current_thread().getName(), int(time.time())))


if __name__ == "__main__":
  token_bucket_filter = TokenBucketFilter(5)
  threads = []
  time.sleep(10)
  for i in range(10):
    threads.append(Thread(target=token_bucket_filter.get_token))

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()