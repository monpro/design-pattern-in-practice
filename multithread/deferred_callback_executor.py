import heapq
import math
import time
from threading import Condition, Thread


class DeferredCallbackExecutor:
  def __init__(self):
    self.actions = []
    self.condition_variable = Condition()
    self.sleep = 0

  def add_action(self, action):
    action.execute_at = time.time() + action.execute_time

    self.condition_variable.acquire()
    heapq.heappush(self.actions, action)
    self.condition_variable.notify()
    self.condition_variable.release()

  def start(self):
    while True:
      self.condition_variable.acquire()

      while len(self.actions) == 0:
        self.condition_variable.wait()

      while len(self.actions) > 0:
        next_action = self.actions[0]
        sleep_time = next_action.execute_time - math.floor(time.time())
        if sleep_time <= 0:
          break

        self.condition_variable.wait(timeout=sleep_time)

      action_to_execute = heapq.heappop(self.actions)
      action_to_execute.action(*(action_to_execute,))
      self.condition_variable.release()


class DeferredAction(object):
  def __init__(self, execute_time, name, action):
    self.execute_time = execute_time
    self.name = name
    self.action = action

  def __lt__(self, other):
    return self.execute_time < other.execute_time


def testAction(action):
  print("{0} executed at {1}, required time: {2}".format(action.name, time.time(), action.execute_time))


if __name__ == "__main__":
  action1 = DeferredAction(3, ("action_1", ), testAction)
  action2 = DeferredAction(2, ("action_2", ), testAction)
  action3 = DeferredAction(5, ("action_3", ), testAction)
  action4 = DeferredAction(4, ("action_4", ), testAction)

  callback_executor = DeferredCallbackExecutor()
  t = Thread(target=callback_executor.start, daemon=True)
  t.start()

  callback_executor.add_action(action1)
  callback_executor.add_action(action2)
  callback_executor.add_action(action3)
  callback_executor.add_action(action4)

  time.sleep(15)