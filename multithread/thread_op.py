from threading import Thread, current_thread


def thread_task(a, b, key1):
  print("{0} received the arguments: {1} {2} {3}".format(current_thread().getName(), a, b, key1))


class ThreadTask(Thread):

  def __init__(self, name, *args):
    Thread.__init__(self, name=name, args=args)

  def run(self):
    print("{0} is running".format(current_thread().getName()))


testThread = Thread(group=None,
                    target=thread_task,
                    name="testThreadCallable",
                    args=(1, 2),  # arguments passed to the target
                    kwargs={'key1': "title"},
                    daemon=None)

threadTask = ThreadTask("testThreadClass")

if __name__ == "__main__":
  testThread.start()
  threadTask.start()

  testThread.join()
  threadTask.join()