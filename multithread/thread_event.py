from threading import Thread, Event
import time


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
      prime_available.wait()
      print(prime_holder)
      prime_holder = None
      prime_available.clear()
      print_finished.set()


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_thread_func():
    global prime_holder
    global found_prime

    i = 1

    while not exit_prog:
        while not is_prime(i):
            i += 1
            time.sleep(.01)

        prime_holder = i
        prime_available.set()
        print_finished.wait()
        print_finished.clear()

        i += 1


if __name__ == "__main__":
  prime_available = Event()
  print_finished = Event()
  exit_prog = False

  printerThread = Thread(target=printer_thread_func)
  printerThread.start()

  finderThread = Thread(target=finder_thread_func)
  finderThread.start()

  # Let the threads run for 3 seconds
  time.sleep(3)

  # Let the threads exit
  exit_prog = True

  printerThread.join()
  finderThread.join()